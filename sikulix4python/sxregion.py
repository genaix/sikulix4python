from typing import Self
from . sxbase import *

class Region(SXBase):
    """
    Wrapper for org.sikuli.script.Region

    - Region() the region of the primary screen
    - Region(x,y,w,h) a region at (x,y) with size (w,h) cropped to the containing screen
    - Region(otherRegion) make an object-copy of object otherRegion
    """

    SXClass = SXRegion

    def hover(self, *args):
        """
        Move the mouse pointer to the given target (args[0])

        if the target is
         - not given, it will be lastMatch or center (if no lastMatch) of this Region
         - an image-filename, a Pattern or an Image, it will first be searched and the valid Match's center/targetOffset will be the target
         - a Match: target will be center/targetOffset of the Match
         - a Region: target will be center of the Region
         - a Location: will be the target

        :param args: see above
        :return: int: 1 if done without errors, 0 otherwise
        """
        if len(args) == 0:
            return self.instance.hover()
        return self.instance.hover(convertArgs(args))

    def click(self, *args):
        if len(args) == 0:
            return self.instance.click()
        elif isinstance(pattern := args[0], Pattern):
            pattern.region(self).click()
        else:
            return self.instance.click(convertArgs(args))

    def highlight(self, *args):
        """
        show a colored frame around the region for a given time or switch on/off

        - **() or (color)** switch on/off with color (default red)

        - **(number) or (number, color)** show in color (default red) for number seconds (cut to int)

        allowed colors given as string
         - a color name out of: black, blue, cyan, gray, green, magenta, orange, pink, red, white, yellow (lowercase and
           uppercase can be mixed, internally transformed to all uppercase)
         - these colornames exactly written: lightGray, LIGHT_GRAY, darkGray and DARK_GRAY
         - a hex value like in HTML: #XXXXXX (max 6 hex digits)
         - an RGB specification as: #rrrgggbbb where rrr, ggg, bbb are integer values in range 0 - 255
           padded with leading zeros if needed (hence exactly 9 digits)

        :param args: a valid combination (see above) or omitted
        :return: self
        """
        if len(args) == 0:
            return self.instance.highlight()
        return self.instance.highlight4py(convertArgs(args))


class Pattern():
    """Обертка для имитации использования Pattern подручными средствами."""

    def __init__(self, image: str, timeout: float = 3.0):
        """Инициализация класса Pattern.

        :param image: имя изображения
        :param timeout: таймаут поиска соответствующего изображения
        :param region: область поиска на экране
        """
        self.region = None
        self.image = image
        self.timeout = timeout
        self.x_offset = None
        self.y_offset = None

    def region(self, region: Region) -> Self:
        """Задать регион поиска."""
        self.region = region
        return self

    def targetOffset(self, x_offset: int, y_offset: int) -> Self:
        """Задать смещение точки для клика.

        :param x_offset: смещение по горизонтали
        :param y_offset: смещение по вертикали
        """
        self.x_offset = x_offset
        self.y_offset = y_offset
        return self

    def click(self):
        """Кликнуть по картинке."""
        match = self.region.exists(self.image, self.timeout) # method missing, wrong signature
        if match:
            match.setTargetOffset(self.x_offset, self.y_offset)
            match.click()
        else:
            raise
