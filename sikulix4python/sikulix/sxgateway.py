"""Sikulix Gateway."""
from py4j.java_gateway import Py4JError, Py4JJavaError
from py4j.protocol import Py4JNetworkError


def convert_args(args):
    """Convert to Java object python args."""
    sxargs = JavaGW.jvm.java.util.ArrayList()
    for arg in args:
        try:
            sxargs.append(arg)
        except Py4JError:
            sxargs.append(arg.instance())
    return sxargs


def sxstart():
    """Start Sikulix connection."""
    from py4j.java_gateway import JavaGateway
    try:
        java_gw = JavaGateway()
        sxpkg = java_gw.jvm.org.sikuli
        return java_gw, sxpkg
    except Py4JNetworkError as e:
        raise ConnectionError("sxstart: SikuliX not running") from e


def sx_class(class_name, pkg_name="script"):
    class_ref = f"SXPKG.{pkg_name}.{class_name}"
    the_class = eval(class_ref, {"SXPKG": SXPKG})
    try:
        the_class.getDefaultInstance4py()
    except Py4JJavaError:
        print(f"sxClass: Class missing: {class_ref}")
        return None
    return the_class


def sx_class_help(class_name, pkg_name="script"):
    the_class = sx_class(class_name, pkg_name)
    if the_class:
        print(the_class.__doc__)
    return the_class


JavaGW, SXPKG = sxstart()
