from __future__ import annotations
from typing import Any, Optional

LB = "\n"
INDENT = "    "
MULTILINE = "\"\"\""


def get_default_list_for_none(inp):
    if inp is not None:
        return inp
    return list()


class Attribute:
    name: str
    type_hint: str = ""
    default: Optional[Any] = None
    comment: str = ""
    index: int
    read_only: bool = False

    def __init__(self, name, type_hint: str = "", default: Optional[Any] = None, comment: str = "", read_only: bool = False):
        self.name = name
        self.type_hint = type_hint
        self.default = default
        self.comment = comment
        self.read_only = read_only

    def __str__(self):
        if not self.read_only:
            string = f"{self.name}"
            if self.type_hint:
                string += f": {self.type_hint}"
            if self.default:
                string += f" = {str(self.default)}"
            return string
        else:
            string = f"@property{LB}"
            string += f"def {self.name}(self)"
            if self.type_hint:
                string += f" -> {self.type_hint}: ..."
            return string

    @staticmethod
    def is_default(attribute: Attribute):
        return attribute.default is not None


class Object:
    name: str
    doc_string: str = ""

    def str_docstring(self):
        if not self.doc_string:
            return ""
        string = f"{INDENT}{MULTILINE}{LB}"
        for line in self.doc_string.splitlines():
            string += f"{INDENT}{line}{LB}"
        string += f"{INDENT}{MULTILINE}{LB}"
        return string

    def str_triple_dots(self):
        return f"{INDENT}...{LB}"

    def remove_comma_space(self, string):
        if string[-2:] == ", ": return string[:-2]
        return string


class Method(Object):
    return_type: str = ""
    paramaters: list[Attribute] = list()

    def __init__(self, name, doc_string: str = "", return_type: str = "", paramaters: list[Attribute] = None):
        self.name = name
        self.doc_string = doc_string
        self.return_type = return_type
        self.paramaters = get_default_list_for_none(paramaters)

    def __str__(self):
        string = f"def {self.name}("
        self.paramaters.sort(key=Attribute.is_default)
        for parameter in self.paramaters:
            string += f"{str(parameter)}, "
        string = self.remove_comma_space(string)
        string += ")"
        if self.return_type:
            string += f" -> {str(self.return_type)}"
        string += f":{LB}"
        string += self.str_docstring()
        string += self.str_triple_dots()
        return string


class Class(Object):
    methods: list[Method] = list()
    attributes: list[Attribute] = list()
    inherit: list[Class] = list()
    sub_cls: list[Class] = list()  # TODO

    def __init__(self, name, doc_string: str = "", return_type: str = "", attributes: list[Attribute] = None, methods: list[Method] = None, inherit: list[Class] = None, sub_cls: list[Class] = None):
        self.name = name
        self.doc_string = doc_string
        self.return_type = return_type
        self.attributes = get_default_list_for_none(attributes)
        self.methods = get_default_list_for_none(methods)
        self.inherit = get_default_list_for_none(inherit)
        self.sub_cls = get_default_list_for_none(sub_cls)

    def str_subcls(self):
        string = ""
        for sub_cls in self.sub_cls:
            for line in str(sub_cls).splitlines():
                string += f"{INDENT}{line}{LB}"
        return string

    def __str__(self):
        string = f"class {self.name}("
        for inherit in self.inherit:
            string += f"{inherit.name}, "
        string = self.remove_comma_space(string)
        string += f"):{LB}"
        string += self.str_docstring()
        for attribute in self.attributes:
            if not attribute.type_hint and not attribute.default:
                attribute.type_hint = "Any"
            for line in str(attribute).splitlines():
                string += f"{INDENT}{line}{LB}"
            if attribute.comment and not attribute.read_only:  # TODO
                string += f"  # {attribute.comment}"
            string += "\n"
        for method in self.methods:
            for line in str(method).splitlines():
                string += f"{INDENT}{line}{LB}"
        string += self.str_subcls()
        string += self.str_triple_dots()
        return string


class PYI:
    imports: list[str] = list()
    methods: list[Method] = list()
    variables: list[Attribute] = list()
    classes: list[Class] = list()

    def __init__(self, imports: list[str] = None, methods: list[Method] = None, variables: list[Attribute] = None, classes: list[Class] = None):
        self.imports = get_default_list_for_none(imports)
        self.methods = get_default_list_for_none(methods)
        self.variables = get_default_list_for_none(variables)
        self.classes = get_default_list_for_none(classes)

    def __str__(self):
        string = ""
        for import_statement in self.imports:
            string += f"{import_statement}{LB}"
        string += f"{LB}"
        for cls in self.classes:
            string += f"{str(cls)}{LB}"
        for method in self.methods:
            string += f"{str(method)}{LB}"
        for var in self.variables:
            string += f"{str(var)}{LB}"
        return string


def test_cases():
    p = Attribute("Animal", type_hint = "str")
    op = Attribute("Name", default = "\"Frieder\"")
    opd = Attribute("Weight", type_hint = "int", default = "15", comment="Put in Kg")
    o = Attribute("Asterisk")
    m = Method("doing_stuff", doc_string = "I do stuff!", return_type = "str", paramaters = [op, p, opd, o])
    x = Method("im_a_function", "This docstring tells you all there is")
    a = Class("Hello", "My favorite time of the year\nis always!", methods = [m,], attributes = [p, op, o, opd])
    b = Class(name = "Submarine", methods = [m,], attributes = [p, op, o, opd])
    c = Class(name = "ALIAS", inherit=[a], sub_cls=[b])
    doc = PYI(imports = ["from typing import Any", "import pymxs"], methods = [x], classes = [a, c], variables = [opd, o, p, op])
    with open('test_cases.pyi', 'w') as file:
        file.write(str(doc))


if __name__ == "__main__":
    test_cases()
