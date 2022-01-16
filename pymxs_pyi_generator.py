import os


def pymxs_get_class_name(obj):
    import pymxs
    return str(pymxs.runtime.classof(obj))


def pymxs_get_obj_from_string(string):
    import pymxs
    try:
        return getattr(pymxs.runtime, string)
    except AttributeError:
        return None


def parse_maxscript_autocomplete():
    path = os.path.split(__file__)[0]
    directory = 'maxscript'
    file_name = 'maxscript.api'
    file_path = os.path.join(path, directory, file_name)
    with open(file_path) as file:
        file_content = file.read()
    analyze = []
    # maxops is an interface
    for line in file_content.splitlines():
        if line.isidentifier():
            analyze.append(line)
        elif all([x.isidentifer() for x in line.split(".")]):
            analyze.append(line)
        else:
            continue
    return [pymxs_get_obj_from_string(x) for x in analyze]


for item in parse_maxscript_autocomplete():
    obj = pymxs_get_obj_from_string(item)
    if not obj:
        continue
    if pymxs_get_class_name(obj) != 'StructDef':
        print(item, pymxs_get_class_name(obj))
