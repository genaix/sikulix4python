"""Sikulix root functions."""

import os

from sikulix4python.sikulix.sxbase import SXApp, SX, SXImagePath
from sikulix4python.sikulix.sxclasses import Screen

SCREEN = Screen()


def reset():
    """Reset params at the start of testing."""
    SX().reset()


def set_bundle_path():
    """Add all files in project to library searching."""
    add_image_path()


def add_image_path(*path):
    """Add path for using images dir."""
    if len(path) == 0:
        import inspect
        stack = inspect.stack()
        a_path = os.path.dirname(stack[1].filename)
        SXImagePath.set_bundle_path(a_path)
        print("setBundlePath:", a_path)
    else:
        for a_path in path:
            SXImagePath.add(a_path)


def open_app(app):
    """Open application."""
    return SXApp(app).open()


def switch_app(app):
    """Switch application."""
    return SXApp(app).focus()


def close_app(app):
    """Close application."""
    return SXApp(app).close()


def click(*args):
    """Click on screen element."""
    return SCREEN.click(*args)


def hover(*args):
    """**hover** Move the mouse pointer to the given target (args[0])

    :param args: see above
    :return: 1 if done without errors, 0 otherwise

    if the target is:
     - not given, it will be lastMatch or center (if no lastMatch) of this Region
     - an image-filename, a Pattern or an Image, it will first be searched and the valid Match's
      center/targetOffset will be the target
     - a Match: target will be center/targetOffset of the Match
     - a Region: target will be center of the Region
     - a Location: will be the target
     - (int, int): explicit target coordinates
    """
    return SCREEN.hover(*args)
