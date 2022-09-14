"""Sikulix extended classes."""

from sikulix4python.sikulix.sxbase import SXScreen, SXBase, SXLocation, SXImage
from sikulix4python.sikulix.sxregion import Region


class Screen(Region):
    """Screen."""

    SXClass = SXScreen


class Location(SXBase):
    """Location."""

    SXClass = SXLocation


class Image(SXBase):
    """Image."""

    SXClass = SXImage
