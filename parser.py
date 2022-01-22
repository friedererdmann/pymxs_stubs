import re


def get_interface_name_from_description(interface_description: str) -> str:
    lines = interface_description.splitlines()
    pattern = r"(?:[\S\s]*):\s+([\S\s]*)"
    match: re.Match
    match = re.match(pattern, lines[0])
    interface_name = match.groups()[0]
    return interface_name


def get_name_and_type_from_definition(definition):
    lines = definition.splitlines()
    definition = lines[0].split(":", maxsplit=1)[0]
    pattern = r"([\S\s]*)\s+(?:\(([\S\s]*)\))"
    match = re.match(pattern, definition)
    if not match:
        return
    name, parent = match.groups()
    parent = parent.replace('const', '')
    parent = parent.replace('system', '')
    parent = parent.strip()
    return name, parent




