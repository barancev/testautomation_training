from selenium import webdriver
import requests
import lxml
from lxml import html
import suds.client


username = "administrator"
password = "root"
base_url = "http://localhost/mantisbt-1.2.19/"


def test_mantis_project_creation_gui():
    project_name = 'project_gui'

    driver = webdriver.Firefox()
    driver.get(base_url + '/login.php')
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_css_selector('input[type=submit]').click()

    driver.get(base_url + '/manage_proj_create_page.php')
    driver.find_element_by_name('name').send_keys(project_name)
    driver.find_element_by_xpath("//input[@type='submit'][@value='Add Project']").click()
    driver.find_element_by_link_text("Proceed").click()

    elements = driver.find_elements_by_xpath("//table[@class='width100'][2]//tr[@class='row-1' or @class='row-2']/td[1]")
    projects = list(map(lambda e: e.text, elements))

    assert project_name in projects

    driver.quit()


def test_mantis_project_creation_http():
    project_name = 'project_http'

    r = requests.post(base_url + '/login.php', data = {'username': username, 'password': password})
    cookies = r.history[0].cookies

    r = requests.get(base_url + '/manage_proj_create_page.php', cookies=cookies)
    tree = lxml.html.fromstring(r.content)
    token = tree.xpath("//input[@name='manage_proj_create_token']")[0].get('value')

    r = requests.post(base_url + '/manage_proj_create.php', cookies=cookies, data =
        {'manage_proj_create_token': token, 'name': project_name, 'description': '',
         'status': '10', 'view_state': '10'})

    r = requests.get(base_url + '/manage_proj_page.php', cookies=cookies)
    tree = lxml.html.fromstring(r.content)
    projects = list(map(lambda e: e.text_content().strip(),
                        tree.xpath("//table[@class='width100'][2]//tr[@class='row-1' or @class='row-2']/td[1]")))

    assert project_name in projects


def test_mantis_project_creation_api():
    service_url = base_url + '/api/soap/mantisconnect.php?wsdl'
    project_name = 'project_api'

    client = suds.client.Client(service_url)

    project = client.factory.create('ProjectData')
    project.name = project_name
    client.service.mc_project_add(username, password, project)

    projects = client.service.mc_projects_get_user_accessible(username, password)

    assert project_name in list(map(lambda p: p.name, projects))
