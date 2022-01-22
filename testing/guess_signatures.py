from ast import expr_context
import re
import inspect
import pymxs

def try_signature(obj, signature=None):
    if not signature:
        signature = list()
    try:
        obj(*signature)
    except RuntimeError as error_message:
        message = str(error_message)
        print(obj, message)
        if message.find("Argument count error:") != -1:
            pattern = r"Argument count error: \S* wanted (\d*), got (\d*)"
            wanted, got = re.findall(pattern, message)[0]
            print(wanted, got)
            new_signature = list(range(int(wanted)))
            return try_signature(obj, new_signature)
        if message.find("Unable to convert:") != -1:
            pattern = r"Unable to convert: (\S*) to type: (\S*)"
            value, exp_type = re.findall(pattern, message)[0]
            print(value, exp_type)
            if exp_type[0] == "<" and exp_type[-1] == ">":
                exp_type = exp_type[1:-1]
            attr = getattr(pymxs.runtime, exp_type)
            attr_type = f"pymxs.runtime.{exp_type}"
            name = f"{exp_type}_{value}"  # assuming value is an int from the range above
            print(f"({name}: {attr_type})\n\n\n\n")
            # new_signature = attr()
            # return try_signature(obj, new_signature)
            #new_signature = signature
            #new_signature[int(value)] = attr()
            # exp_type = f"({exp_type}_0: pymxs.runtime.{exp_type})"
        if message.find("Type error:") != -1 and message.find("requires") != -1:
            pattern = r"Type error: (\S*) requires (\S*), got: (\S*)"
            method, exp_type, value = re.findall(pattern, message)[0]
            print(method, exp_type, value)
            if exp_type[0] == "<" and exp_type[-1] == ">":
                exp_type = exp_type[1:-1]
            attr = getattr(pymxs.runtime, exp_type)
            attr_type = f"pymxs.runtime.{exp_type}"
            name = f"{exp_type}_{value}"  # assuming value is an int from the range above
            print(f"({name}: {attr_type})\n\n\n\n")
        if message.find("Type error:") != -1 and message.find("needs a") != -1:
            pattern = r"(?:Type error: )(\S*) needs a ([\s\S]*) got: , got: (\S)*"
            try:
                method, exp_types, value = re.findall(pattern, message)[0]
                print(exp_types.split("or"))
            except IndexError:
                print(message)

            # new_signature = attr()
            # return try_signature(obj, new_signature)
        return ""
        if message.find("The function needed arguent with value:") != -1:
            pattern = r"(?:Runtime error: The function needed argument with value:)([\s\S]*), got: (\S*)"
            exp_types, value = re.findall(pattern, message)[0]
            exp_types = exp_types.replace("#", "")
            types = exp_types.split("|")
            print(types)

def get_method_signature(obj):
    signature = None
    empty = "()"
    try:
        signature = str(inspect.signature(obj))
    except ValueError:
        #signature = empty
        #if not signature:
        signature = try_signature(obj)
    print(signature)
    return signature

# get_method_signature(pymxs.undo)
# get_method_signature(pymxs.runtime.AverageSelVertCenter)
# get_method_signature(pymxs.runtime.EulerToQuat)
# get_method_signature(pymxs.runtime.AddSubRollout)
get_method_signature(pymxs.runtime.AppendSubSelSet)
get_method_signature(pymxs.runtime.ArbAxis)
get_method_signature(pymxs.runtime.AssignNewName)
get_method_signature(pymxs.runtime.AttachObjects)
get_method_signature(pymxs.runtime.AverageSelVertCenter)
get_method_signature(pymxs.runtime.AverageSelVertNormal)
get_method_signature(pymxs.runtime.AxisTripodLocked)
# get_method_signature(pymxs.runtime.BoxPickNode)
# get_method_signature(pymxs.runtime.CRTCheckAssert)
# get_method_signature(pymxs.runtime.CRTCheckMemory)
# get_method_signature(pymxs.runtime.CRTCorruptHeap)
# get_method_signature(pymxs.runtime.CRTheapcheck)
# get_method_signature(pymxs.runtime.CaptureCallStack)
# get_method_signature(pymxs.runtime.CheckForSave)
# get_method_signature(pymxs.runtime.CirclePickNode)
# get_method_signature(pymxs.runtime.ClearCurSelSet)
# get_method_signature(pymxs.runtime.ClearNodeSelection)
# get_method_signature(pymxs.runtime.ClearSubSelSets)
# get_method_signature(pymxs.runtime.CloseActiveShade)
# get_method_signature(pymxs.runtime.CommitControllerValue)
# get_method_signature(pymxs.runtime.CompleteRedraw)
# get_method_signature(pymxs.runtime.ConfigureBitmapPaths)
# get_method_signature(pymxs.runtime.ConvertDirIDToInt)
# get_method_signature(pymxs.runtime.ConvertIntToDirID)
# get_method_signature(pymxs.runtime.ConvertKelvinToRGB)
# get_method_signature(pymxs.runtime.ConvertToBody)
# get_method_signature(pymxs.runtime.ConvertToBodyCutter)
# get_method_signature(pymxs.runtime.ConvertToJoinBodies)
# get_method_signature(pymxs.runtime.CreateDialog)
# get_method_signature(pymxs.runtime.CreateLockKey)
# get_method_signature(pymxs.runtime.CreatePreview)
# get_method_signature(pymxs.runtime.CrowdAreaDrawing)
# get_method_signature(pymxs.runtime.CrowdAreaEnd)
# get_method_signature(pymxs.runtime.CrowdAreaGetActiveTool)
# get_method_signature(pymxs.runtime.CrowdAreaGetAddMode)
# get_method_signature(pymxs.runtime.CrowdAreaGetBrushSize)
# get_method_signature(pymxs.runtime.CrowdAreaGetBrushSizePath)
# get_method_signature(pymxs.runtime.CrowdAreaGetCircleSides)
# get_method_signature(pymxs.runtime.CrowdAreaGetConstriant)
# get_method_signature(pymxs.runtime.CrowdAreaGetNode)
