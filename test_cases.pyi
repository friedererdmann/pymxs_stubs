from typing import Any
import pymxs

class Hello():
    """
    My favorite time of the year
    is always!
    """
    Animal: str
    Name = "Frieder"
    Asterisk: Any
    Weight: int = 15  # Put in Kg
    def doing_stuff(Animal: str, Asterisk: Any, Name = "Frieder", Weight: int = 15) -> str:
        """
        I do stuff!
        """
        ...
    ...

class ALIAS(Hello):
    class Submarine():
        Animal: str
        Name = "Frieder"
        Asterisk: Any
        Weight: int = 15  # Put in Kg
        def doing_stuff(Animal: str, Asterisk: Any, Name = "Frieder", Weight: int = 15) -> str:
            """
            I do stuff!
            """
            ...
        ...
    ...

def im_a_function():
    """
    This docstring tells you all there is
    """
    ...

Weight: int = 15
Asterisk: Any
Animal: str
Name = "Frieder"
