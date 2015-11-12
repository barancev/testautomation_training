from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_gui():
    driver = webdriver.Firefox()
    driver.get("http://selenium2.ru/")
    assert driver.current_url == "http://selenium2.ru/"
    search_field = driver.find_element_by_name("searchword")
    search_field.clear()
    search_field.send_keys("python" + Keys.ENTER)
    result = driver.find_element_by_css_selector("div.searchintro")
    assert result.text == "Результат поиска: найдено 39 объектов."
    driver.quit()

