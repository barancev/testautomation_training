from selenium.webdriver.support.color import Color


def test_isolated_component():
    assert Color.from_string("#ffffff") == Color(255, 255, 255)
