"""Sikulix Region."""

from sikulix4python.sikulix.sxbase import SXBase, SXRegion
from sikulix4python.sikulix.sxgateway import convert_args


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
         - an image-filename, a Pattern or an Image, it will first be searched and the valid
         Match's center/targetOffset will be the target
         - a Match: target will be center/targetOffset of the Match
         - a Region: target will be center of the Region
         - a Location: will be the target

        :param args: see above
        :return: int: 1 if done without errors, 0 otherwise
        """
        if len(args) == 0:
            return self.instance.hover()
        return self.instance.hover(convert_args(args))

    def click(self, *args):
        """Click on screen according to suitable image."""
        if len(args) == 0:
            return self.instance.click()
        elif isinstance(pattern := args[0], Pattern):
            pattern.set_region(self).click()
        else:
            return self.instance.click(convert_args(args))

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
        return self.instance.highlight4py(convert_args(args))

    def wait(self, target: str, timeout: int = None):
        """Wait for element present.

        :param target: target image to wait
        :param timeout: time to wait for
        :return: int: 1 if done without errors, 0 otherwise
        """
        if timeout is None:
            return self.instance.wait(target)
        return self.instance.wait(target, float(timeout))

    def waitVanish(self, target: str, timeout: int = None):
        """Wait for element not present.

        :param target: target image to wait
        :param timeout: time to wait for
        :return: int: 1 if done without errors, 0 otherwise
        """
        if timeout is None:
            return self.instance.waitVanish(target)
        return self.instance.waitVanish(target, float(timeout))

    def exists(self, target: str, timeout: int = None):
        """Check for element present.

        :param target: target image to wait
        :param timeout: time to wait for
        :return: a Match object that contains the best match.
        None is returned, if nothing is found within the specified waiting time.
        """
        if timeout is None:
            return self.instance.exists(target)
        return self.instance.exists(target, float(timeout))

    def type(self, *args):
        """Type text to area.

        target is target image for typing
        text is text for typing

        :param args: see above
        :return: int: 1 if done without errors, 0 otherwise
        """
        if len(args) == 0:
            return self.instance.type()
        else:
            return self.instance.type(*args)


class Pattern:
    """Wrapper for similar using Pattern workaround."""

    def __init__(self, image: str, timeout: float = 3.0):
        """Инициализация класса Pattern.

        :param image: image name
        :param timeout: timeout for search corresponding image
        """
        self.region = None
        self.image = image
        self.timeout = timeout
        self.x_offset = None
        self.y_offset = None

    def set_region(self, region: Region) -> "Pattern":
        """Set region for search."""
        self.region = region
        return self

    def targetOffset(self, x_offset: int, y_offset: int) -> "Pattern":
        """Set offset point for click.

        :param x_offset: x-axis offset
        :param y_offset: y-axis offset
        """
        self.x_offset = x_offset
        self.y_offset = y_offset
        return self

    def click(self):
        """Click on image."""
        match = self.region.exists(self.image, self.timeout)  # method missing, wrong signature
        if match:
            match.setTargetOffset(self.x_offset, self.y_offset)
            match.click()
        else:
            raise
