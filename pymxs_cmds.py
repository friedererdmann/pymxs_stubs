from typing import Any, List
import pymxs


def strip_string_stream(string):
    start = 'StringStream:"'
    end = '"'
    return string[len(start):-len(end)]


def get_pymxs_obj_from_name(arg: str) -> Any:
    full_path = f"pymxs.runtime.{arg}"
    module, attr = full_path.rsplit(".", maxsplit=1)
    try:
        module = eval(module)
    except AttributeError:
        return None
    try:
        return getattr(module, attr)
    except AttributeError:
        return None


def pymxs_apropos(arg: str = "") -> str:
    string_stream = pymxs.runtime.stringStream('')
    pymxs.runtime.apropos(arg, to=string_stream)
    return strip_string_stream(str(string_stream))


def pymxs_get_core_interfaces() -> List[pymxs.runtime.interface]:
    result = pymxs.runtime.getCoreInterfaces()
    return list(result)


def pymxs_show_properties(obj: Any) -> str:
    """Requires an initialized object"""
    string_stream = pymxs.runtime.stringStream('')
    pymxs.runtime.showProperties(obj, to=string_stream)
    return strip_string_stream(str(string_stream))


def pymxs_show_interfaces(cls: Any) -> str:
    string_stream = pymxs.runtime.stringStream('')
    pymxs.runtime.showInterfaces(cls, to=string_stream)
    return strip_string_stream(str(string_stream))


def pymxs_show_interface(interface: Any) -> str:
    string_stream = pymxs.runtime.stringStream('')
    pymxs.runtime.showInterface(interface, to=string_stream)
    return strip_string_stream(str(string_stream))


def pymxs_show_class(arg: str = "") -> str:
    string_stream = pymxs.runtime.stringStream('')
    pymxs.runtime.showClass(arg, to=string_stream)
    return strip_string_stream(str(string_stream))


def pymxs_show_class_description(arg: str = "") -> str:
    return pymxs_show_class(f"{arg}.*")


def pymxs_get_interfaces(cls: Any) -> str:
    result = pymxs.runtime.getInterfaces(cls)
    return [str(x) for x in result]


def pymxs_classof(cls: Any) -> str:
    """pymxs.runtime.box returns <node<GeometryClass>> returns GeometryClass

    Args:
        cls (Any): A class or object that you want to inspect

    Returns:
        str: Name of parent class
    """
    return str(pymxs.runtime.classof(cls))


def pymxs_get_prop_names(obj: Any) -> List[str]:
    """Returns a list of all property names of the base object.

    Args:
        obj (Any): A class or object that you want to inspect

    Returns:
        List[str]: List of all property names
    """
    result = pymxs.runtime.getPropNames(obj)
    return [str(x) for x in result]
