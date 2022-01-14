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
    """"Format pymxs.runtime method names to be all lower case"""
    if is_generated_code(obj):
        method_name = name.lower()
    else:
        method_name = name
    return method_name


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
        # print(x,y,type_name)
        if type_name in ["function", "builtin_function_or_method", "method_descriptor"]:
            method_name = format_method_name(name, obj)
            signature = get_method_signature(name, obj)
            if name in ["getmxsprop", "setmxsprop"]:
                if module not in [pymxs.MXSWrapperBase, pymxs.MXSWrapperObjectSet, pymxs.MXSWrapperObjectSetIter]:
                    continue
                if name == "getmxsprop": signature = "(self, key: str)"
                if name == "setmxsprop": signature = "(self, key: str, value)"
            functions = f"{base_indent}def {method_name}{signature}: ..."
            if output:
                print(functions)
            lines.append(functions)
        elif type_name in classes:
            class_name = format_class_name(name, obj)
            classes.append(class_name)
            class_of = str(pymxs.runtime.classof(obj))
            parent_class = format_class_name(class_of)
            if class_of == "PyWrapperBase":
                parent_class = ""
            if parent_class == class_name:
                parent_class = ""
            class_definition = f"{base_indent}class {class_name}({parent_class}):"
            if output:
                print(class_definition)
            lines.append(class_definition)
            try:
                prop_names = pymxs.runtime.GetPropNames(obj)
            except RuntimeError:
                pass
            else:
                instance = obj()
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
                        if output:
                            print(property_definition)
                        lines.append(property_definition)
            closing_dots = f"{one_indent}..."
            if output:
                print(closing_dots)
            lines.append(closing_dots)
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
