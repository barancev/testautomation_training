import requests
import lxml
from lxml import html
import suds.client


def test_mantis_project_creation_http():
    username = "administrator"
    password = "root"
    base_url = "http://localhost/mantisbt-1.2.19/"

    project_name = 'project1'

    r = requests.post(base_url + '/login.php', data =
        {'username': username, 'password': password})
    cookies = r.history[0].cookies

    r = requests.get(base_url + '/manage_proj_create_page.php', cookies=cookies)
    tree = lxml.html.fromstring(r.content)
    token = tree.xpath("//input[@name='manage_proj_create_token']")[0].get('value')

    r = requests.post(base_url + '/manage_proj_create.php', cookies=cookies, data =
        {'manage_proj_create_token': token, 'name': project_name, 'description': '',
         'status': '10', 'view_state': '10'})

    # ---------------- API -------------------

    service_url = "http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl"
    client = suds.client.Client(service_url)
    projects = client.service.mc_projects_get_user_accessible(username, password)

    assert project_name in list(map(lambda p: p.name, projects))

    # ---------------- API -------------------
