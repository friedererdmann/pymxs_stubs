import os
import inspect
import keyword
import pymxs


SPACE = "    "
BASE_CLASS_TYPES = ["type", "class", "runtime"]


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
        pass
    else:
        try:
            instance = obj()
        except RuntimeError:
            pass
        else:
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
    return None


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
        full_name = repr(obj)
        if keyword.iskeyword(full_name) or "#Struct" in full_name:
            continue
        type_name = type(obj).__name__
        parent_class = get_parent_class_name(obj)
        # print(x,y,type_name)
        if type_name in ["function", "builtin_function_or_method", "method_descriptor"] or parent_class in ["Primitive"]:
            line = write_method(name, obj, module, base_indent)
            lines = append_and_print(lines, line, output)
        elif type_name in classes:
            class_name = format_class_name(name, obj)
            classes.append(class_name)
            class_definition = write_class(class_name, obj, base_indent)
            lines = append_and_print(lines, class_definition, output)
            property_definition = find_properties(obj, one_indent)
            lines = append_and_print(lines, property_definition, output)
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
