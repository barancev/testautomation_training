import suds
import suds.client
import pytest

username = "administrator"
password = "root"


@pytest.fixture
def client():
    service_url = "http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl"
    return suds.client.Client(service_url)


@pytest.mark.parametrize("project_name", ["x"])
def test_mantis_project_creation_positive(client, project_name):
    project = client.factory.create('ProjectData')
    project.name = project_name
    project_id = client.service.mc_project_add(username, password, project)

    projects = client.service.mc_projects_get_user_accessible(username, password)

    assert project.name in list(map(lambda p: p.name, projects))

    assert client.service.mc_project_delete(username, password, project_id)


@pytest.mark.parametrize("project_name", ["", " "])
def test_mantis_project_creation_negative(client, project_name):
    project = client.factory.create('ProjectData')
    project.name = project_name

    with pytest.raises(suds.WebFault) as exeption:
        project_id = client.service.mc_project_add(username, password, project)

    projects = client.service.mc_projects_get_user_accessible(username, password)

    assert project.name not in list(map(lambda p: p.name, projects))

