import suds.client
import pytest
import string
import random

@pytest.fixture
def client():
    service_url = "http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl"
    return suds.client.Client(service_url)


def pytest_generate_tests(metafunc):
    if 'project_name' in metafunc.fixturenames:
        names = [''.join(random.choice(string.ascii_letters + string.digits) for _ in range(2**i)) for i in range(10)]
        metafunc.parametrize("project_name", names)


def test_mantis_project_creation(client):
    username = "administrator"
    password = "root"
    project_name = "project1"

    project = client.factory.create('ProjectData')
    project.name = project_name
    project_id = client.service.mc_project_add(username, password, project)

    projects = client.service.mc_projects_get_user_accessible(username, password)

    assert project.name in list(map(lambda p: p.name, projects))

    assert client.service.mc_project_delete(username, password, project_id)