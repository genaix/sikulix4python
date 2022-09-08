# https://www.python.org should be opened in Safari
from time import sleep
from pathlib import Path

from sikulix4python import addImagePath, switchApp, openApp, Region, sxClassHelp

IMAGES_DIR = str(Path(__file__).parent.joinpath("images").absolute())

# reset the state of SikuliX
# only needed, but recommended in main script
addImagePath(IMAGES_DIR)
# print(sxClassHelp("Location")); exit()
#hover(100,100); exit()

# openApp("VirtualBoxVM")
# switchApp("VirtualBoxVM")
# reg_1 = Region(3,43,2042,1047)
def run_test():
    sleep(3)

    reg_1 = Region()
    reg_1.click("1661954192601.png")
    reg_1.click("1661954111162.png")
    reg_1.wait("1661954274248.png")
    reg_1.type("1661954274248.png", "jz1@devmail.stageoffice.ru")
    reg_1.click(Pattern("1661954308546.png").targetOffset(0, 5))
    reg_1.type("1661954308546.png", "jz123!@#JZ123")
    reg_1.click("1661954339274.png")
    reg_1.waitVanish("1661954339274.png")
    reg_1.wait("1661955298515.png", 1)


# reg = Region()
# print(reg)
# reg.setX(100).setW(300)
# print(reg)
# hover()
# hover(reg)
#
# exit()

# make images available in the folder of the script
# addImagePath()
#
# switchApp("safari")
#
# hover() # undotted uses SCREEN object (sxundotted)
#
# scr = Screen()

# getCenter() is found auto-magically,
# though not defined in the Python class Screen
# see sxclasses::__getattr__
# one gets method missing, if signatures do not fit
# scr.getCenter().grow(100).highlight(2)
#
# img = "img.png" # located via ImagePath

# a Match object is completely handled at the Java level
# not defined at the Python level
# match = scr.exists(img, 3) # method missing, wrong signature
# match = scr.exists(img, 3.0) # number must be floated/double
# if match:
#     match.highlight(2)
#     match.click()
