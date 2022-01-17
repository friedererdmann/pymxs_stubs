import re
import pymxs
from itertools import tee

INTERFACE = "Interface:"
PROPERTIES = "Properties:"
METHODS = "Methods:"
ACTIONS = "Actions:"
SPACE = "    "

INTERFACES = []
METHOD_LIST = []


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def format_class_name(name, obj=None):
    if name.startswith("<") and name.endswith(">"):
        name = name[1:-1]
    if name.startswith("&"): name = name[1:]
    if name == "runtime":
        return name
    if not obj:
        method_name = name.title()
    else:
        method_name = name
    class_name = ""
    for i, l in enumerate(zip(name, method_name)):
        if l[0].isupper():
            class_name += l[0]
        else:
            class_name += l[1]
    if class_name == "Void":
        class_name = "None"
    class_name = class_name.replace(" ", "")
    return class_name


def strip_string_stream(string):
    start = 'StringStream:"'
    end = '"'
    return string[len(start):-len(end)]


def parse_property(string_list):
    VALIDATION = "Validated by "
    WRITE = "Write"
    property = string_list[0]
    comments = string_list[1:]
    name, value, mode = property.split(" : ")
    name = name[1:].upper()
    value = format_class_name(value)
    comment_str = ""
    pattern = r"#([\w]*)"
    find_comments = re.compile(pattern)
    for comment in comments:
        if " enums:" in comment:
            values = find_comments.findall(comment)
            comment_str = f"# {', '.join(values)} - rt.Name(\"\")"
        else:
            comment_str = f"# {comment}"
    if VALIDATION in mode:
        validation = mode.split(VALIDATION)[-1]
        comment_str += f"# {validation}"
    if WRITE not in mode:
        print(f"{SPACE}@property")
        print(f"{SPACE}def {name}() -> {value}: ...")
    else:
        print(f"{SPACE}{name}: {value}  {comment_str}")


def parse_methods(string_list):
    global METHOD_LIST
    signature = string_list[0]
    comments = string_list[1:]
    pattern = r"(<[A-Za-z\s&\d]*>)([A-Za-z]+)"
    return_name, *mandatory_parameters = re.findall(pattern, signature)
    pattern = r"([A-Za-z]+):(<[A-Za-z\s&\d]*>)"
    optional_parameters = re.findall(pattern, signature)
    return_value = format_class_name(return_name[0])
    method_name = format_class_name(return_name[1])
    method_string = f"{SPACE}def {method_name}("

    for parameter in mandatory_parameters:
        value = format_class_name(parameter[0])
        name = format_class_name(parameter[1])
        method_string += f"{name}: {value}, "

    for parameter in optional_parameters:
        name = format_class_name(parameter[0])
        value = format_class_name(parameter[1])
        line = [comment for comment in comments if comment.lower().find(f"{name.lower()} default value:") != -1][0]
        comments.remove(line)
        default_value = line.split(": ")[1]
        if default_value in ("true", "false"):
            default_value = default_value.title()
        method_string += f"{name}: {value} = {default_value}, "

    if method_string[-1] == " ": method_string = method_string[:-2]
    method_string += f") -> {return_value}:"
    if method_string in METHOD_LIST:
        return
    if [line for line in METHOD_LIST if line.startswith(f"def {method_name}(")]:
        print(f"{SPACE}@overload")
    METHOD_LIST.append(method_string)
    print(method_string)
    if comments:
        print(f"{SPACE}{SPACE}\"\"\"")
        for comment in comments:
            print(f"{SPACE}{SPACE}{comment}")
        print(f"{SPACE}{SPACE}\"\"\"")
    print(f"{SPACE}{SPACE}...")


def parse_strings(string_list, signifier=".", output=parse_property):
    properties = []
    property = []
    for i, line in enumerate(string_list):
        content = line.strip()
        if content.startswith(signifier):
            if property:
                properties.append(property)
            property = [content]
        else:
            property.append(content)
    if property:
        properties.append(property)
    for property in properties:
        output(property)
    return properties


def parse_interface(string_list):
    global METHOD_LIST
    interface_name = format_class_name(string_list[0].strip()[len(INTERFACE)+1:])
    if interface_name in INTERFACES:
        return
    INTERFACES.append(interface_name)
    print(f"class {interface_name}(pymxs.runtime.Interface):")
    property_line = string_list.index(f"   {PROPERTIES}")
    method_line = string_list.index(f"   {METHODS}")
    action_line = string_list.index(f"   {ACTIONS}")
    properties_lines = string_list[property_line+1:method_line]
    parse_strings(properties_lines, ".", parse_property)
    methods = string_list[method_line+1:action_line]
    METHOD_LIST = []
    parse_strings(methods, "<", parse_methods)
    actions = string_list[action_line+1:]
    # not relevant for pymxs (?) - e.g. pymxs.runtime.FixAmbient
    # print(actions)
    print(f"{SPACE}...")


def parse_for_interfaces(string):
    interfaces_string = strip_string_stream(string)

    lines = interfaces_string.splitlines()

    interface_lines = []

    for i, line in enumerate(lines):
        if line.strip().startswith("Interface:"):
            interface_lines.append(i)

    interface_lines.append(len(lines))

    interface_borders = list(pairwise(interface_lines))

    for interface in interface_borders:
        parse_interface(lines[interface[0]:interface[1]])


def parse_node_interfaces(node):
    string_stream = pymxs.runtime.stringStream('')
    pymxs.runtime.showInterfaces(node, to=string_stream)
    parse_for_interfaces(str(string_stream))


parse_node_interfaces(pymxs.runtime.Node)
