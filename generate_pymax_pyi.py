import os
import inspect
import pymxs


def get_dir(name, indentation=0, classes=None, output=False):
    python_keywords = ["from", "class", "assert", "break"]
    if not classes:
        classes = ["type", "class", "runtime"]
    space = "    "
    lines = []
    for x in dir(name):
        if not x.startswith("__") or x.startswith("%") or x.startswith("3") or x.startswith("+") or x.startswith("=") or x.startswith("?"):
            y = getattr(name, x)
            type_name = type(y).__name__
            # print(x,y,type_name)
            if type_name in ["function", "builtin_function_or_method", "method_descriptor"]:
                try:
                    signature = str(inspect.signature(y))
                except ValueError:
                    signature = "()"
                if x == "getmxsprop":
                    if indentation:
                        continue
                    signature = "(self, key: str)"
                if x == "setmxsprop":
                    if indentation:
                        continue
                    signature = "(self, key: str, value)"
                functions = "{2}def {0}{1}: ...".format(x, signature, space*indentation)
                if output:
                    print(functions)
                lines.append(functions)
            elif type_name in classes:
                if "#" in repr(y) or "%" in repr(y) or "+" in repr(y) or "=" in repr(y) or x.startswith("3") or repr(y).startswith("("):
                    continue
                if x in python_keywords or repr(y) in python_keywords:
                    continue
                classes.append(x)
                inherit = str(pymxs.runtime.classof(y))
                if inherit == "PyWrapperBase":
                    inherit = ""
                class_definition = "{2}class {0}({1}):".format(x, inherit,space*indentation)
                if output:
                    print(class_definition)
                lines.append(class_definition)
                try:
                    prop_names = pymxs.runtime.GetPropNames(y)
                except RuntimeError:
                    pass
                else:
                    for prop in prop_names:
                        if str(prop) in python_keywords:
                            continue
                        try:
                            typehint = type(getattr(y(), str(prop))).__name__
                            if typehint == "NoneType":
                                typehint = "None"
                        except (RuntimeError, AttributeError):
                            pass
                        else:
                            property_definition = "{2}{0}: {1}".format(prop, typehint, space*(indentation+1))
                            if output:
                                print(property_definition)
                            lines.append(property_definition)
                lines.append("{0}...".format(space*(indentation+1)))
                if not indentation:
                    increment = indentation + 1
                    sub_lines = get_dir(y, increment, classes)
                    lines += sub_lines
    return lines


def run():
    output = get_dir(pymxs, indentation=0)
    directory, _ = os.path.split(__file__)
    filename = "pymxs.pyi"
    filepath = os.path.join(directory, filename)
    with open(filepath, "w") as file:
        for line in output:
            file.write(line + "\n")


run()
