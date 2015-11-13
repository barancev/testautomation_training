from suds.client import Client
import xmltodict


def test_soap_weather():
    client = Client("http://www.webservicex.net/globalweather.asmx?wsdl")

    xml_text = client.service.GetWeather("Moscow", "Russia")
    res = xmltodict.parse(xml_text)

    assert res['CurrentWeather']['Status'] == 'Success'
    print(res)
