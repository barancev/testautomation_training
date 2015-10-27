from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import UnexpectedTagNameException
from selenium.webdriver.common.alert import Alert


def test_without_isolation():
    driver = webdriver.Firefox()
    driver.get("http://selenium2.ru/")
    element = driver.find_element_by_tag_name("div")
    try:
        select = Select(element)
        assert False
    except UnexpectedTagNameException:
        pass


def test_with_isolation(mocker):
    with mocker.patch('selenium.webdriver.remote.webelement.WebElement') as MockElement:
        element = MockElement.return_value
        element.tag_name = 'div'

        try:
            select = Select(element)
            assert False
        except UnexpectedTagNameException:
            pass


def test_with_isolation_and_check(mocker):
    with mocker.patch('selenium.webdriver.remote.webdriver.WebDriver') as MockDriver:
        driver = MockDriver.return_value

        alert = Alert(driver)
        alert.accept()

        driver.execute.assert_called_with("acceptAlert")