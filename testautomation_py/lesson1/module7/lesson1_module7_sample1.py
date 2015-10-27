import requests


def test_server_part():
    res = requests.get("http://selenium2.ru/")

    assert res.status_code == 200
    assert "Selenium WebDriver" in res.text
