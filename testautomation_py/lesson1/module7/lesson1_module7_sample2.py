import requests


def test_server_part():
    payload = {"part": "sele", "pos": "4", "n": "5", "v": "4"}
    res = requests.get("https://suggest.yandex.ru/suggest-ya.cgi", params=payload)

    assert res.status_code == 200
    x = eval(res.text)
    assert x[0] == "sele"
    assert "selenium" in x[1]
