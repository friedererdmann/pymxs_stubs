We can gather information on maxscript and pymxs from these locations/methods:

- Maxscript API Autocomplete
  - Text document meant for autocompletion
  - Not sure yet what the outcome is
- (`pymxs.runtime.`) `apropos`
  - Returns all variables in the current scope of Max.
  - Similar output to the Maxscript API Autocomplete but not complete overlap
  - Parser in `get_all.py`
- (`pymxs.runtime.`) `showInterfaces`
  - Method to inspect for SOME classes what interfaces they have
  - Gets us a view on the underlying interface classes and their actions, methods and attributes (properties)
  - A whitelist and blacklist of known inspectable classes is in `get_all.py`
- `dir()` in python on `pymxs` and its members
  - Done in `generate_pymaxs_pyi.py` (this is the first version of this pyi)
  - Inspect all members of an element in Python
- (`pymxs.runtime.`)`GetPropNames`
  - Get attributes (properties) of (initialized) objects
- (`pymxs.runtime.`)`classof`
  - Gets the class of an object
- Online Documentation
  - HTML Scraper in `html_scraper.py` can scrape pages for text
  - Difficult to match and generalize but could provide good docstrings
  - Less feasible for the moment
- Guessing Signatures
  - Script in `guess_signatures.py` to run a Python method over and over again parsing Error Messages to see what the expected signature is
  - Doesn't seem feasible at the moment
- Manually authored pyi files
  - A number of people have started writing pyi files from scratch
  - The system should allow to have a place to push manually written pyi files and merge them in
  - e.g. check for good hand written doc strings or fixes to signatures (needs a model to describe changes)
- Per class inspection:
```python
node = pymxs.runtime.box
print("__str__", str(node))  # Box
print("__repr__", repr(node))  # <GeometryClass<Box>>
print("__dir__", dir(node))  # ['getmxsprop', 'setmxsprop']
print("new arguments", inspect.signature(node.__new__))  # (*args, **kwargs)
print("rt.classof", pymxs.runtime.classof(node))  # GeometryClass
print("type", type(node))  # <class 'pymxs.MXSWrapperBase'>
print("type name", type(node).__name__)  # MXSWrapperBase
print("type module", type(node).__module__)  # pymxs
a = pymxs.runtime.stringStream('')
pymxs.runtime.showInterfaces(node, to=a)
print("rt.showInterfaces", str(a))
"""
  Interface: realWorldMapSizeInterface
   Properties:
    .realWorldMapSize : boolean : Read|Write
   Methods:
   Actions:
"""
b = pymxs.runtime.stringStream('')
pymxs.runtime.apropos(str(node),to=b, implicitWild=False)  # Box (const MAXClass): Box
print("rt.apropos", str(b))
c = pymxs.runtime.stringStream('')
pymxs.runtime.showClass(str(node),to=c)  # Box : GeometryClass {10,0}
print("rt.showClass", str(c))
d = pymxs.runtime.stringStream('')
pymxs.runtime.showClass(str(node)+".*",to=d)
print("rt.showClass wildcard", str(d))
"""
Box : GeometryClass {10,0}
  .typeinCreationMethod (Creation_Method) : integer
  .typeInPos (Type_in_Position) : point3
  .typeInLength (Length) : float
  .typeInWidth (Width) : float
  .typeInHeight (Height) : float
  .length : worldUnits
  .width : worldUnits
  .height : worldUnits
  .widthsegs (Width_Segments) : integer
  .lengthsegs (Length_Segments) : integer
  .heightsegs (Height_Segments) : integer
  .mapCoords (Generate_Texture_Coords) : boolean
"""
obj = node()
print(dir(obj))
# ['getmxsprop', 'height', 'heightsegs', 'length', 'lengthsegs', 'mapcoords', 'realWorldMapSize', 'setmxsprop', 'typeInHeight', 'typeInLength', 'typeInPos', 'typeInWidth', 'typeinCreationMethod', 'width', 'widthsegs']
```
