from . sxgateway import *

SX = SXPKG.script.SX
SXRegion = SXPKG.script.Region
SXScreen = SXPKG.script.Screen
SXLocation = SXPKG.script.Location
SXImage = SXPKG.script.Image
SXImagePath = SXPKG.script.ImagePath
SXApp = SXPKG.script.App

class SXBase():

    SXClass = SX

    def __init__(self, *args):
        try:
            self.instance = self.SXClass.getDefaultInstance4py()
            if len(args) > 0:
                self.instance = self.SXClass.make4py(convertArgs(args))
        except Exception as e:
            raise Exception("Class not prepared for SikuliX") from e

    def __str__(self):
        return self.instance.toString()

    def __getattr__(self, item):
        currentObject = self.instance;

        def temp_method(*args, **kwargs):
            mCall = item + "("
            mCallError = "" + mCall
            countArgs = len(args)
            if countArgs > 0:
                mCall += "args[0]"
                mCallError += "%s" % (args[0])
            for nArg in range(1, countArgs):
                mCall += ", args[%d]" % nArg
                mCallError += ", %s" % (args[nArg])
            mCall += ")"
            mCallError  += ")"
            try:
                toEval = "currentObject." + mCall
                result = eval(toEval, {"currentObject": self.instance, "args": args})
                return result
            except:
                print(f"Method missing: {currentObject}::{mCallError}")
                return currentObject

        return temp_method

