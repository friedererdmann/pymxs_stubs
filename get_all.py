# inspect all classes and variables in maxscript scope with apropos
# parse output somewhat
# generate list of classes that can be inspected with showInterfaces

# Split classes by if they can be inspected with ShowInterfaces
BLACKLIST = ("Generic", "<internal>", "Primitive", "Interface", "Integer", "String", "UndefinedClass", "StructDef", "RolloutClass", "MAXScriptFunction", "NodeGeneric", "BooleanClass", "Color", "Class", "PxCreationPlaceAndSizeTool", "BipedGeneric", "Float", "Array", "Name", "MouseTool", "dotNetObject", "WindowStream", "Integer64", "NURBSGenericMethodsWrapper", "HKey", "MappedPrimitive", "StringStream", "Time", "Point3", "MappedGeneric", "ObjectSet", "UserGeneric", "CurveCtlGeneric", "MAXBezierShapeClass", "OkClass", "UnsuppliedClass", "EmptyClass", "NoValueClass", "Point2", "MAXMeshClass", "SelectionSetArray", "Interval")
WHITELIST = ("MAXClass", "MSPluginClass", "MSCustAttribDef", "MAXSuperClass", "StandardMaterialClass", "MAXTVNode", "MAXRefTarg", "Control", "MaterialLibrary", "MAXRootScene", "MAXRootNode", "IObject", "Material_Editor")

def get_every_max_class():
    with open("output.txt") as file:
        return file.read()
    import pymxs
    string_stream = pymxs.runtime.stringStream('')
    pymxs.runtime.apropos("", to=string_stream)
    return str(string_stream)


def strip_string_stream(string):
    start = 'StringStream:"'
    end = '"'
    return string[len(start):-len(end)]


def even(integer):
    return integer//2 == integer/2


def get_variable_descriptions_from_max():
    output = strip_string_stream(get_every_max_class()).splitlines()

    variables = []
    variable = []
    quote_count = 0
    bracket_count = 0
    stay_open = False
    for i, line in enumerate(output):
        prev_quote_count = quote_count
        quote_count += line.count("\"")
        # if i > 8070 and i < 8330:
        #     print(i, stay_open, quote_count, line)
        if line.startswith(('  ','\t','\"', "(", ")")) or stay_open or not line:
            variable.append(line)
            if even(quote_count):
                stay_open = False
            continue
        if not even(quote_count):
            stay_open = True
        else:
            stay_open = False
        if variable and not stay_open:
            variables.append(variable)
            quote_count = 0
        variable = [line]
    if variable:
        variables.append(variable)

    classes = set()

    for i, var in enumerate(variables):
        # if len(var) > 1 or len(var[0]) > 80:
        #     for line in var:
        #         print(line)
        #     print(50*"=")
        a = var[0].split(":", maxsplit=1)
        b = a[0].split(" ", maxsplit=1)
        var_name = b[0]
        c = b[1]
        if c.startswith("(") and c.endswith(")"):
            c = c[1:-1]
        d = c.split(" ", maxsplit=1)
        class_name = d[-1]
        if not class_name.isidentifier():
            continue
        const = False
        if d[0] == 'const':
            const = True
        if not "." in var_name and class_name not in BLACKLIST:
                print(f"pymxs.runtime.{var_name}")# of type {class_name}")
        if var_name == "MeshDeformPW": return
        classes.add(class_name)
    print(classes)


get_variable_descriptions_from_max()
