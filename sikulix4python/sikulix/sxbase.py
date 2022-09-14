"""Sikulix basic class."""

from py4j.java_gateway import Py4JJavaError
from sikulix4python.sikulix.sxgateway import SXPKG, convert_args

SX = SXPKG.script.SX
SXRegion = SXPKG.script.Region
SXScreen = SXPKG.script.Screen
SXLocation = SXPKG.script.Location
SXImage = SXPKG.script.Image
SXImagePath = SXPKG.script.ImagePath
SXApp = SXPKG.script.App


class SXBase:
    """Basic class of Sikulix objects."""
    SXClass = SX

    def __init__(self, *args):
        """Create object."""
        try:
            self.instance = self.SXClass.getDefaultInstance4py()
            if len(args) > 0:
                self.instance = self.SXClass.make4py(convert_args(args))
        except Py4JJavaError as e:
            raise Exception("Class not prepared for SikuliX") from e

    def __str__(self):
        """String representation."""
        return self.instance.toString()

    def __getattr__(self, item):
        """Call object attribute."""
        current_object = self.instance

        def temp_method(*args):
            m_call = item + "("
            m_call_error = "" + m_call
            count_args = len(args)
            if count_args > 0:
                m_call += "args[0]"
                m_call_error += str(args[0])
            for nArg in range(1, count_args):
                m_call += f", args[{nArg}]"
                m_call_error += f", {args[nArg]}"
            m_call += ")"
            m_call_error += ")"
            try:
                to_eval = "current_object." + m_call
                result = eval(to_eval, {"current_object": self.instance, "args": args})
                return result
            except RuntimeError:
                print(f"Method missing: {current_object}::{m_call_error}")
                return current_object

        return temp_method
