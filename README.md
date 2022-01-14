# PyMXS Stubs generator

## What

Pymxs, the 3DsMax bindings of Maxscript to Python doesn't come with any stubs.
This is an attempt at generating stubs automatically by inspecting running code.

## Generate stubs
Run `generate_pymax_pyi.py` in 3DsMax to generate stubs. Tested with 3DsMax 2021 (Python3).

## Use stubs
Copy the `pymxs.pyi` file to a path where you'd usually be able to call `import pymxs` from.
> These Stubs come as they are: I make no promises that they work or cover all your needs.

## Development
- Open Directory in VSCode
- Pick the 3Ds Max Python as your interpreter
- Unzip [latest MXSPyCom Release](https://github.com/techartorg/MXSPyCOM/releases) into `/mxspycom`
- Run `debug/start_debug.py` in Max
- Run Debug configuration `Python: Remote Attach`
- Run task `Execute Script in 3Ds Max` on `generate_pymax_pyi.py` file

## Current scope
- Works in 3Ds Max 2021
- Works with Python 3
- Gets properties of most 3DsMax objects

### Missing from current version (to do)
- Signatures for max script calls (need to go into `__new__` constructors of the objects)
- Some properties get skipped as the object they belong to can't be generated without the correct signature
- No `#Struct` object types
- No properties for regular object types (like Array)
- Not all properties have the right hint (alot will still say `None` because they need initialization)
- Some Max Scene clean up before, after, during script exectuion (this creates a TON of objects in your Max Scene)
- Check other performance optimizations like turn off viewport rendering as applicable
- Checking if everything is correct, including order of the pyi
- Captialization rules - right now names are read as is, but might be worth enforcing some lowercase or CamelCase rules
- Less hacky code
- Streamline debug/development process
- Encoding definition of pyi file
- `Callable` for properties/arguments that need it

## Contributing

Please feel free to fork and push Pull Requests my way. Also issues are welcome - in that case please include as much detail as possible.

## Thanks
- [MXSPyCOM](https://github.com/techartorg/MXSPyCOM) for easy debugging
- [TechArt.org](https://techart.online/) for the constant help

## Autodesk License
3Ds Max, the maxscript API, pymxs and all other items belong to Autodesk.
