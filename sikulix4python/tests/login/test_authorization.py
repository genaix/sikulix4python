from pathlib import Path
from time import sleep

from pytest import mark
from sikulix4python.sikulix.sxregion import Region, Pattern
from sikulix4python.sikulix.sxundotted import add_image_path

IMAGES_DIR = str(Path(__file__).parent.joinpath("images").absolute())

add_image_path(IMAGES_DIR)
# print(sx_class_help("Location"))


@mark.de
def test_authorization():
    """Пример теста авторизации в плагине."""
    sleep(3)

    reg_1 = Region()
    reg_1.click("1663245463523.png")
    reg_1.click("1663245503415.png")
    reg_1.wait("1663245556288.png")
    reg_1.type("1663245556288.png", "jz1@devmail.stageoffice.ru")
    reg_1.click(Pattern("1663245589070.png").targetOffset(-14, 4))
    reg_1.type("1663245589070.png", "jz123!@#JZ123")
    reg_1.click("1663245698748.png")
    reg_1.waitVanish("1663245698748.png")
    reg_1.wait("1663252241627.png", 10)
    match = reg_1.exists("1663245698748.png", 2)
    assert not match, "Должен успешно авторизоваться"
    reg_1.rightClick(Pattern("1663252241627.png").targetOffset(-4, 13))
