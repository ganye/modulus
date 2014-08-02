from .base import BaseColor

def CustomColor(attr=0, fgrd=256, bgrd=0):
    return type('CustomColor', (BaseColor,), dict(attr=attr, fgrd=fgrd,
        bgrd=bgrd))
