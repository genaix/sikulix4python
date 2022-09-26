from pathlib import Path
from time import sleep

from pytest import mark
from sikulix4python.sikulix.sxregion import Pattern
from sikulix4python.sikulix.sxundotted import add_image_path, click, wait, waitVanish, type

IMAGES_DIR = str(Path(__file__).parent.joinpath("images").absolute())

add_image_path(IMAGES_DIR)


@mark.de
def test_example():
    """Description."""
    sleep(3)

    click("1664201796413.png")
    click("1664201826959.png")
    wait("1664201863210.png", 3)
    type("1664201863210.png", "jz1@devmail.stageoffice.ru")
    click(Pattern("1664201947147.png").targetOffset(-76, 8))
    type("jz123!@#JZ123")
    click("1664202026847.png")
    waitVanish("1664202026847.png")
    wait("1664209544002.png", 5)
    sleep(1)
    click(Pattern("1664209544002.png").targetOffset(-80, 116))
