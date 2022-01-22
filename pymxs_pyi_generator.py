import sys
import os
import re
import pymxs
import importlib

from typing import List

from testing.new_test import Interface

path = os.path.split(__file__)[0]
if not path in sys.path:
    sys.path.append(path)
import pyi_generator
importlib.reload(pyi_generator)
import helper
importlib.reload(helper)
import pymxs_cmds
importlib.reload(pymxs_cmds)
import parser
importlib.reload(parser)


CLASSES = dict()


def check_item_list(list_of_strings):
    valid_items = []
    for item in list_of_strings:
        obj = pymxs_cmds.get_pymxs_obj_from_name(item)
        if obj is not None:
            valid_items.append(item)
    return valid_items


def split_apropos_output_into_parts(apropos: str) -> List[str]:
    continuation_symbols = ('  ','\t','\"', "(", ")")
    chunks = list()
    chunk = ""
    stay_open: bool = False
    quotations: int = 0
    for line in apropos.splitlines():
        quotations += line.count("\"")
        if line.startswith(continuation_symbols) or stay_open or not line:
            chunk += f"\n{line}"
            if helper.even(quotations):
                stay_open = False
            continue
        if not helper.even(quotations):
            stay_open = True
        else:
            stay_open = False
        if chunk and not stay_open:
            chunks.append(chunk)
            quotations = 0
        chunk = line
    if chunk:
        chunks.append(chunk)
    return chunks


def split_interface_definitions(string: str) -> List[str]:
    interfaces = list()
    lines = string.splitlines()
    interface = ""
    for line in lines:
        if line.strip().startswith("Interface:"):
            if interface:
                interfaces.append(Interface)
            interface = line
        else:
            interface += f"\n{line}"
    if interface:
        interfaces.append(Interface)
    return interfaces


def get_interface_definitions_from_obj(obj) -> List[str]:
    interfaces_description = pymxs_cmds.pymxs_show_interfaces(obj)
    definitions = split_interface_definitions(interfaces_description)
    return definitions


def get_interface_names_for_obj(obj):
    interfaces = get_interface_definitions_from_obj(obj)
    interface_names = list()
    for interface in interfaces:
        name = parser.get_interface_name_from_description(interface)
        interface_names.append(name)
    return interface_names


def get_pyi_classes_from_list(name_list):
    classes = list()
    for name in name_list:
        if name not in CLASSES:
            CLASSES[name] = pyi_generator.Class(name)
        classes.append(CLASSES[name])
    return classes


def analyze_structdef_definition(definition):
    lines = definition.splitlines()
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
    interface_chunks = get_interface_definitions_from_obj(obj)
    attributes = list()
    functions = list()
    for chunk in interface_chunks:
        name = parser.get_interface_name_from_description(chunk)
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
    obj = pymxs_cmds.get_pymxs_obj_from_name(name)
    max_base_class = pymxs_cmds.pymxs_classof(obj)
    interfaces = get_interface_names_for_obj(obj)
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


# with open(helper.relative_file("apropros.txt"), "w") as file:
#     file.write(helper.pymxs_apropos())


# write_apropos_chunk_files()

apropos = pymxs_cmds.pymxs_apropos()
definitions = split_apropos_output_into_parts(apropos)
parents = list()
for i, definition in enumerate(definitions):
    name, parent = parser.get_name_and_type_from_definition(definition)
    parents.append(parent.lower())
    if not name.isidentifier() or name in ["nvpxText"]:
        continue
    if parent == "Internal":
        continue
    # generate_class(name, [parent])
    # if parent == 'StructDef':
    #     functions, data = analyze_structdef_definition(definition)
    #     add_methods_and_members_to_struct_def(name, functions, data)
for name in list(set(parents)):
    print(name)
# pyi = pyi_generator.PYI(classes=CLASSES.values())
# with open(helper.relative_file('new_test.pyi'), 'w') as file:
#     file.write(str(pyi))

