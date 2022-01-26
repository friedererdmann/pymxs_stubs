import os
import inspect
import keyword
import re
import traceback
import pymxs

from pymxs import runtime as mxRt
from collections import defaultdict


SPACE = "    "
BASE_CLASS_TYPES = ["type", "class", "runtime"]
MXS_TO_PY_TYPES = {
    "void": None,
    "node": mxRt.Node,
    "matrix3": mxRt.Matrix3,
    "boolean": bool,
    "integer": int,
    "float": float,
}


def get_struct_definition(struct_data):
    struct_data = str(struct_data)
    def collect_metadata(interface_data):
        interface_data = list(map(str.strip, interface_data))
        properties_line_start = interface_data.index("Properties:")
        properties_line_end = interface_data.index("Methods:")
        methods_line_start = properties_line_end
        methods_line_end = interface_data.index("Actions:")
        actions_line_start = methods_line_end
        data = defaultdict(list)
        for line_index, line in enumerate(interface_data):
            if not line or line == '"':
                continue

            if line_index > properties_line_start and line_index < properties_line_end:
                data["properties"].append(line)
            if line_index > methods_line_start and line_index < methods_line_end:
                data["methods"].append(line)
            if line_index > actions_line_start:
                data["actions"].append(line)

        return data

    def collect_method_arguments(method_data):
        out_method_data = defaultdict(lambda: defaultdict(list))
        for data in method_data:
            arguments = data.split("<")
            return_type, method_name = arguments[1].split(">")
            clean_method_name = method_name.rstrip("()").strip()
            # out_method_data[clean_method_name]["return_type"] = MXS_TO_PY_TYPES[return_type]
            out_method_data[clean_method_name]["signature"] = data
            out_method_data[clean_method_name]["return_type"] = return_type
            if method_name.endswith("()"):
                continue
            out_method_data[clean_method_name]["arguments"] = [
                {key: val for (key,val) in zip(("type", "name"), _split.split(">")) } for _split in arguments if _split
            ]

        return out_method_data

    if "(const Interface):" in struct_data or "(const StructDef)" in struct_data:
        # struct_name = for a = 1 to streamLine.Count while streamLine[a] != " " do structName += streamLine[a]
        struct_name = struct_data.split()[0]
        struct = mxRt.Execute(struct_name)
        interface_stream = mxRt.StringStream("")
        mxRt.ShowInterface(struct, to=interface_stream)
        interface_data = str(interface_stream).splitlines()
        metadata = collect_metadata(interface_data)
        method_data = collect_method_arguments(metadata["methods"])

        return method_data


def get_struct_definitions(print_output=False):
    data = {}
    globals_stream = mxRt.StringStream("")
    mxRt.Apropos("", to=globals_stream)
    mxs_globals = str(globals_stream).splitlines()
    for obj in mxs_globals:
        try:
            metadata = get_struct_definition(obj)
            if not metadata:
                continue

            struct_name = obj.split()[0]
            data[struct_name] = metadata
        except KeyError:
            traceback.print_exc()
        except Exception:
            pass

    if print_output:
        for k, v in data.items():
            print(k)
            for _k, _v in v.items():
                print(f"-- {_k}:")
                for __k, __v in _v.items():
                    print(f"---- {__k}:")
                    if isinstance(__v, str):
                        print(f"------ {__v}:")
                        continue
                    for ___v in __v:
                        for ____k, ____v in ___v.items():
                            print(f"------ {____k}:")
                            print(f"-------- {____v}")


def is_generated_code(obj):
    try:
        inspect.getfile(obj)
    except TypeError:
        return True
    return False


def format_method_name(name, obj):
    if name in ["getmxsprop", "setmxsprop", "run_redo", "run_undo"]:
        return name
    return format_class_name(name, obj)
    # """"Format pymxs.runtime method names to be all lower case"""
    # if is_generated_code(obj):
    #     method_name = name.lower()
    # else:
    #     method_name = name
    # return method_name


def format_class_name(name, obj=None):
    if name.startswith("<") and name.endswith(">"):
        name = name[1:-1]
    if name.startswith("&"): name = name[1:]
    name = name.replace(" ", "")
    if name == "runtime":
        return name
    if not obj:
        method_name = name.title()
    elif is_generated_code(obj):
        method_name = name.title()
    else:
        method_name = name
    class_name = ""
    for i, l in enumerate(zip(name, method_name)):
        if l[0].isupper():
            class_name += l[0]
        else:
            class_name += l[1]
    return class_name


def get_method_signature(name, obj):
    try:
        signature = str(inspect.signature(obj))
    except ValueError:
        signature = "()"
    return signature


def write_method(name, obj, module, base_indent):
    method_name = format_method_name(name, obj)
    signature = get_method_signature(name, obj)
    if name in ["getmxsprop", "setmxsprop"]:
        if module not in [pymxs.MXSWrapperBase, pymxs.MXSWrapperObjectSet, pymxs.MXSWrapperObjectSetIter]:
            return None
        if name == "getmxsprop": signature = "(self, key: str)"
        if name == "setmxsprop": signature = "(self, key: str, value)"
    functions = f"{base_indent}def {method_name}{signature}: ..."
    return functions


def get_parent_class_name(obj):
    class_of = str(pymxs.runtime.classof(obj))
    parent_class = format_class_name(class_of)
    return parent_class


def write_class(class_name, obj, base_indent):
    parent_class = get_parent_class_name(obj)
    if parent_class == "PyWrapperBase":
        parent_class = ""
    if parent_class == class_name:
        parent_class = ""
    class_definition = f"{base_indent}class {class_name}({parent_class}):"
    return class_definition


def find_properties(obj, one_indent):
    try:
        prop_names = pymxs.runtime.GetPropNames(obj)
    except RuntimeError:
        return None
    try:
        instance = obj()
    except RuntimeError:
        return None
    properties = []
    for prop in prop_names:
        prop_name = str(prop).upper()  # moving property names to upper to avoid keyword conflicts
        if not prop_name.isidentifier() or keyword.iskeyword(prop_name):
            continue
        try:
            typehint = type(getattr(instance, prop_name)).__name__
        except (RuntimeError, AttributeError):
            pass
        else:
            if typehint == "NoneType":
                typehint = "None"
            property_definition = f"{one_indent}{prop_name}: {typehint}"
            properties.append(property_definition)
    properties = list(set(properties))
    properties.sort()
    return properties


def find_interfaces(obj, one_indent):
    lines = []
    skip = ["Event",
            "ExportMesh()"]
    if str(obj).startswith(("DYNFUN", "Px", "px")) or str(obj) in skip:
        return lines
    try:
        instance = obj()
    except (RuntimeError, TypeError):
        return None
    res = pymxs.runtime.stringStream('')
    try:
        pymxs.runtime.showInterfaces(instance, to=res)
    except RuntimeError:
        return None
    output = str(res).splitlines()
    mode = ""
    methods = []
    new_method = []
    for line in output:
        line_content = line.strip()
        if line_content == "Properties:":
            mode = ""
            continue
        elif line_content == "Methods:":
            mode = "Methods"
            continue
        elif line_content == "Actions:":
            if new_method:
                methods.append(new_method)
                new_method = []
            mode = ""
            continue
        if mode == "Methods":
            if line_content.startswith("<"):
                if new_method:
                    methods.append(new_method)
                new_method = []
                new_method.append(line_content)
            new_method.append(line_content)
    for method in methods:
        definition = method[0]
        pattern = r"(<[A-Za-z\s&\d]*>)([A-Za-z]+)"
        return_name, *mandatory_parameters = re.findall(pattern, definition)
        pattern = r"([A-Za-z]+):(<[A-Za-z\s&\d]*>)"
        optional_parameters = re.findall(pattern, definition)
        return_class, method_name = return_name
        return_type = format_class_name(return_class)
        if return_type == "Void":
            return_type = "None"
        else:
            return_type = "runtime." + return_type
        parameters = {format_class_name(name): "runtime." + format_class_name(class_type) for class_type, name in mandatory_parameters}
        optional_parameters = {format_class_name(name): "runtime." + format_class_name(class_type) for name, class_type in optional_parameters}
        params = str(parameters)[1:-1].replace("'","")
        optionals = str(optional_parameters)[1:-1].replace("'","")
        if params and optionals:
            params += ","
        method_name = format_class_name(method_name)
        lines.append(f"{one_indent}def {method_name}({params} {optionals}) -> {return_type}: ...")
    lines.sort()
    return lines
    # print(methods)


def append_and_print(lines, line, output=False):
    if isinstance(line, str):
        if output: print(line)
        lines.append(line)
    if isinstance(line, list):
        if output:
            for entry in line: print(entry)
        lines += line
    return lines


def get_dir(module, indentation=0, classes=None, output=False):
    base_indent = SPACE * indentation
    one_indent = SPACE * (indentation+1)
    if not classes:
        classes = BASE_CLASS_TYPES
    lines = []
    for name in dir(module):
        if not name.isidentifier() or keyword.iskeyword(name) or name.startswith("__") or "unknown" in name.lower():
            continue
        obj = getattr(module, name)
        try:
            full_name = repr(obj)
        except RuntimeError:
            continue
        if keyword.iskeyword(full_name):
            continue
        if "#Struct" in full_name:
            pass
        type_name = type(obj).__name__
        parent_class = get_parent_class_name(obj)
        # print(x,y,type_name)
        if type_name in ["function", "builtin_function_or_method", "method_descriptor"] or parent_class in ["Primitive", "MAXScriptFunction"]:
            line = write_method(name, obj, module, base_indent)
            lines = append_and_print(lines, line, output)
        elif type_name in classes:
            class_name = format_class_name(name, obj)
            classes.append(class_name)
            class_definition = write_class(class_name, obj, base_indent)
            lines = append_and_print(lines, class_definition, output)
            property_definition = find_properties(obj, one_indent)
            lines = append_and_print(lines, property_definition, output)
            interface_definition = find_interfaces(obj, one_indent)
            lines = append_and_print(lines, interface_definition, output)
            closing_dots = f"{one_indent}..."
            lines = append_and_print(lines, closing_dots, output)
            if not indentation:
                # currently only one level of recursion
                increment = indentation + 1
                sub_lines = get_dir(obj, increment, classes)
                lines += sub_lines
    return lines


def run():
    output = get_dir(pymxs, indentation=0, output=True)
    directory, _ = os.path.split(__file__)
    filename = "pymxs.pyi"
    filepath = os.path.join(directory, filename)
    with open(filepath, "w") as file:
        for line in output:
            file.write(line + "\n")


run()
get_struct_definitions()


# for k, v in data["autosave"].items():
#     print(k)
#     print(v)

# data = "<boolean>CopyData <node>srcnode <node>dstnode"
# split = data.split("<")
# for s in split:
#     print(s)

# print([{key: val for (key,val) in zip(("type", "name"), _split.split(">")) } for _split in split if _split])