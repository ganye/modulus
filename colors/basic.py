from .base import BaseColor

__all__ = ['Black', 'Red', 'Green', 'Yellow', 'Blue', 'Magenta', 'Cyan',
        'White']

class Black(BaseColor):
    fgrd = 30

class Red(BaseColor):
    fgrd = 31

class Green(BaseColor):
    fgrd = 32

class Yellow(BaseColor):
    fgrd = 33

class Blue(BaseColor):
    fgrd = 34

class Magenta(BaseColor):
    fgrd = 35 

class Cyan(BaseColor):
    fgrd = 36

class White(BaseColor):
    fgrd = 97
