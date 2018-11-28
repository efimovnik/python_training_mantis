from model.project import Project
from suds.client import Client
from suds import WebFault


class SoapHelper:

    def __init__(self, app, name=None, description=None):
        self.app = app
        self.name = name
        self.description = description

    global client
    client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")

    def can_login(self, username, password):
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        list = []
        projects = client.service.mc_projects_get_user_accessible("administrator", "root")
        for project in projects:
            name = project.name
            description = project.description
            list.append(Project(name=name, description=description))
        return list