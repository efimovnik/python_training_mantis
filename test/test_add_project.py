
from model.project import Project

def test_add_project(app, json_projects):
    project = json_projects
    old_contacts = app.project.get_project_list()
    app.project.create(project)
    new_contacts = app.project.get_project_list()
    assert len(new_contacts) == len(old_contacts) + 1
    old_contacts.append(project)
    assert sorted(new_contacts) == sorted(old_contacts)
    #print(app.project.get_project_list())


