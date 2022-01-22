import sys
import os
import re
import pymxs
import importlib
from typing import List
from itertools import tee

path = os.path.split(__file__)[0]
if not path in sys.path:
    sys.path.append(path)
import pyi_generator
importlib.reload(pyi_generator)


CLASSES = dict()


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def even(integer):
    return integer//2 == integer/2


def relative_file(file_name):
    path = os.path.split(__file__)[0]
    return os.path.join(path, file_name)


def strip_string_stream(string):
    start = 'StringStream:"'
    end = '"'
    return string[len(start):-len(end)]


def pymxs_get_class_name(obj):
    return str(pymxs.runtime.classof(obj))


def pymxs_get_interface_descriptions(obj):
    a = pymxs.runtime.stringStream('')
    try:
        pymxs.runtime.showInterfaces(obj, to=a)
    except RuntimeError:
        pass
    return strip_string_stream(str(a))


def pymxs_get_obj_from_string(string):
    module_name = "pymxs.runtime"
    if "." in string:
        index = string.rfind(".")
        path = string[:index]
        string = string[index+1:]
        module_name += f".{path}"
    try:
        module = eval(module_name)
    except AttributeError:
        return None
    try:
        return getattr(module, string)
    except AttributeError:
        return None


def generate_apropos_list():
    string_stream = pymxs.runtime.stringStream('')
    pymxs.runtime.apropos("", to=string_stream)
    return strip_string_stream(str(string_stream))


def parse_maxscript_autocomplete():
    with open(relative_file('maxscript/maxscript.api')) as file:
        file_content = file.read()
    analyze = []
    for line in file_content.splitlines():
        if line.isidentifier():
            analyze.append(line)
        elif all([x.isidentifier() for x in line.split(".")]):
            analyze.append(line)
        else:
            continue
    return analyze


def check_item_list(list_of_strings):
    valid_items = []
    for item in list_of_strings:
        obj = pymxs_get_obj_from_string(item)
        if obj is not None:
            valid_items.append(item)
    return valid_items


def split_apropos_output_into_chunks(apropos):
    chunks = list()
    chunk = list()
    stay_open = False
    quotations = 0
    for line in apropos.splitlines():
        quotations += line.count("\"")
        if line.startswith(('  ','\t','\"', "(", ")")) or stay_open or not line:
            chunk.append(line)
            if even(quotations):
                stay_open = False
            continue
        if not even(quotations):
            stay_open = True
        else:
            stay_open = False
        if chunk and not stay_open:
            chunks.append(chunk)
            quotations = 0
        chunk = [line]
    if chunk:
        chunks.append(chunk)
    return chunks


def write_apropos_chunk_files():
    apropos = generate_apropos_list()
    chunks = split_apropos_output_into_chunks(apropos)
    for i, chunk in enumerate(chunks):
        with open(relative_file(f"apropos\\{i:04}.txt"), "w") as file:
            for line in chunk:
                file.write(f"{line}\n")


def get_interface_name(string_list):
    pattern = r"(?:[\S\s]*):\s+([\S\s]*)"
    match: re.Match
    match = re.match(pattern, string_list[0])
    interface_name = match.groups()[0]
    # parse and create the rest of the interface parser.py
    return interface_name


def break_interface_string_to_chunks(string):
    interfaces = list()
    lines = string.splitlines()
    interface_lines = list()
    for i, line in enumerate(lines):
        if line.strip().startswith("Interface:"):
            interface_lines.append(i)
    interface_lines.append(len(lines))
    interface_borders = list(pairwise(interface_lines))
    for interface in interface_borders:
        interfaces.append(lines[interface[0]:interface[1]])
    return interfaces


def get_interfaces_as_chunks(obj):
    interfaces_description = pymxs_get_interface_descriptions(obj)
    interfaces = break_interface_string_to_chunks(interfaces_description)
    return interfaces


def get_interface_names(obj):
    interfaces = get_interfaces_as_chunks(obj)
    interface_names = list()
    for interface in interfaces:
        name = get_interface_name(interface)
        interface_names.append(name)
    return interface_names


def get_pyi_classes_from_list(name_list):
    classes = list()
    for name in name_list:
        if name not in CLASSES:
            CLASSES[name] = pyi_generator.Class(name)
        classes.append(CLASSES[name])
    return classes


def get_name_and_type_from_chunk(chunk):
    if isinstance(chunk, str):
        lines = chunk.splitlines()
    else:
        lines = chunk
    definition = lines[0].split(":", maxsplit=1)[0]
    pattern = r"([\S\s]*)\s+(?:\(([\S\s]*)\))"
    match = re.match(pattern, definition)
    if not match:
        return
    name, parent = match.groups()
    parent = parent.replace('const', '')
    parent = parent.replace('system', '')
    parent = parent.strip()
    return format_class_name(name), format_class_name(parent)


def analyze_structdef_chunk(chunk):
    if isinstance(chunk, str):
        lines = chunk.splitlines()
    else:
        lines = chunk
    data = list()
    functions = list()
    pattern = r"\s+(\w*):<(\w*)>;\s+(\w*)"
    struct_member = re.compile(pattern)
    for line in lines:
        match = struct_member.match(line)
        if not match:
            continue
        name, kind, public = match.groups()
        if public == 'private':
            continue
        if kind == 'fn':
            functions.append(name)
        elif kind == 'data':
            data.append(name)
    return functions, data


def add_methods_and_members_to_struct_def(cls_name, functions, data):
    cls: pyi_generator.Class
    cls = get_pyi_classes_from_list([cls_name])[0]
    for function in functions:
        method = pyi_generator.Method(format_class_name(function))
        cls.methods.append(method)
    for attribute in data:
        prop = pyi_generator.Attribute(format_class_name(attribute))
        cls.attributes.append(prop)


def format_class_name(name, obj=None):
    if name.startswith("<") and name.endswith(">"):
        name = name[1:-1]
    if name.startswith(("&", ".")): name = name[1:]
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


def parse_property(string_list):
    VALIDATION = "Validated by "
    WRITE = "Write"
    property = string_list[0]
    comments = string_list[1:]
    name, value, mode = property.split(" : ")
    name = format_class_name(name)
    comment_str = ""
    pattern = r"#([\w]*)"
    find_comments = re.compile(pattern)
    for comment in comments:
        if " enums:" in comment:
            values = find_comments.findall(comment)
            comment_str = f"{', '.join(values)} - rt.Name(\"\")"
        else:
            comment_str = f"{comment}"
    if VALIDATION in mode:
        validation = mode.split(VALIDATION)[-1]
        comment_str += f"{validation}"
    read_only = (WRITE not in mode)
    return pyi_generator.Attribute(name, value, comment=comment_str, read_only=read_only)


def parse_methods(string_list):
    signature = string_list[0]
    comments = string_list[1:]
    pattern = r"(<[A-Za-z\s&\d]*>)([A-Za-z]+)"
    return_name, *mandatory_parameters = re.findall(pattern, signature)
    pattern = r"([A-Za-z]+):(<[A-Za-z\s&\d]*>)"
    optional_parameters = re.findall(pattern, signature)
    return_value = format_class_name(return_name[0])
    method_name = format_class_name(return_name[1])
    parameters = list()
    for parameter in mandatory_parameters:
        value = format_class_name(parameter[0])
        name = format_class_name(parameter[1])
        parameters.append(pyi_generator.Attribute(name, value))
    for parameter in optional_parameters:
        name = format_class_name(parameter[0])
        value = format_class_name(parameter[1])
        line = [comment for comment in comments if comment.lower().find(f"{name.lower()} default value:") != -1][0]
        comments.remove(line)
        default_value = line.split(": ")[1]
        if default_value in ("true", "false"):
            default_value = default_value.title()
        parameters.append(pyi_generator.Attribute(name, value, default=default_value))
    comment_str = ""
    for line in comments:
        comment_str += f"{line.strip()}\n"
    return pyi_generator.Method(method_name, comment_str, return_value, parameters)


def parse_strings(string_list, signifier=".", output=parse_property):
    properties = []
    attributes = []
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
        attributes.append(output(property))
    return attributes


def build_interfaces(obj):
    interface_chunks = get_interfaces_as_chunks(obj)
    attributes = list()
    functions = list()
    for chunk in interface_chunks:
        name = get_interface_name(chunk)
        property_line = chunk.index(f"   Properties:")
        method_line = chunk.index(f"   Methods:")
        action_line = chunk.index(f"   Actions:")
        properties_lines = chunk[property_line+1:method_line]
        attributes = parse_strings(properties_lines, ".", parse_property)
        methods = chunk[method_line+1:action_line]
        functions = parse_strings(methods, "<", parse_methods)
        actions = chunk[action_line+1:]
        # not relevant for pymxs (?) - e.g. pymxs.runtime.FixAmbient
        # print(actions)
        if name == "Class": inherit = list()  # This should not inherit from anything
        CLASSES[name] = pyi_generator.Class(name, attributes=attributes, methods=functions)


def generate_class(name, parents: List[str] = None):
    if "." in name:
        index = name.find(".")
        parent = name[:index]
        if parent not in CLASSES:
            generate_class(parent)
        CLASSES[parent].sub_cls.append(generate_class(name[index+1:], parents))
        return
    obj = pymxs_get_obj_from_string(name)
    max_base_class = pymxs_get_class_name(obj)
    interfaces = get_interface_names(obj)
    build_interfaces(obj)
    if not parents:
        parents = list()
    parent_names = list(set([*parents, max_base_class, *interfaces]))
    if name in parent_names:
        parent_names.remove(name)
    parent_classes = get_pyi_classes_from_list(parent_names)
    if name == "Class": inherit = list()  # This should not inherit from anything
    CLASSES[name] = pyi_generator.Class(name, inherit=parent_classes)
    return CLASSES[name]


# items = parse_maxscript_autocomplete()
# valid = check_item_list(items)
# print(len(items), len(valid))

# with open(relative_file("apropros.txt"), "w") as file:
#     file.write(generate_apropos_list())


# write_apropos_chunk_files()

apropos = generate_apropos_list()
chunks = split_apropos_output_into_chunks(apropos)
for i, chunk in enumerate(chunks):
    name, parent = get_name_and_type_from_chunk(chunk)
    if not name.isidentifier() or name in ["nvpxText"]:
        continue
    if parent == "Internal":
        continue
    generate_class(name, [parent])
    if parent == 'StructDef':
        functions, data = analyze_structdef_chunk(chunk)
        add_methods_and_members_to_struct_def(name, functions, data)

pyi = pyi_generator.PYI(classes=CLASSES.values())
with open(relative_file('new_test.pyi'), 'w') as file:
    file.write(str(pyi))

