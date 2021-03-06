import abc
from collections.abc import Generator
from typing import Callable

# manual testing file
# handwritten signatures for testing
# trying mypy on __init__.py


# from __init__.py
def print_(*args) -> None: ...
def attime(time) -> Generator[None, None, None]: ...
def atlevel(node_name) -> Generator[None, None, None]: ...
def undo(onoff, label: str = ...) -> Generator[None, None, None]: ...
def quiet(onoff) -> Generator[None, None, None]: ...
def redraw(onoff) -> Generator[None, None, None]: ...
def animate(onoff) -> Generator[None, None, None]: ...
def mxstoken() -> Generator[None, None, None]: ...
def mxsreference(o): ...
def byref(o): ...


# from pymxs.pyd
class MXSWrapperBase(abc.ABC):
    @abc.abstractmethod
    def getmxsprop(self, key: str):
        """Explicitly get a MXS property. Useful for accessing MXS nested property."""
        ...

    @abc.abstractmethod
    def setmxsprop(self, key: str, value):
        """Explicitly set a MXS property. Useful for accessing MXS nested property."""
        ...


class MXSWrapperObjectSet(MXSWrapperBase): ...


class MXSWrapperObjectSetIter(MXSWrapperObjectSet): ...


def __bootstrap_mxs() -> None: ...


def contextmanager(func: Callable) -> Callable: ...


class maxlistener(abc.ABC):
    @staticmethod
    def write(text: str) -> bool: ...


def run_redo() -> None: ...
def run_undo() -> None: ...

class runtime(abc.ABC):
    class execute(MXSWrapperBase):
        def __new__(cls, command: str) -> MXSWrapperBase: ...
