from model.project import Project

def test_add_project(app, db, json_projects):
    project = json_projects
    old_projects_db = db.get_project_list()
    old_projects_soap = app.soap.get_project_list()
    app.project.create(project)
    new_projects_db = db.get_project_list()
    new_projects_soap = app.soap.get_project_list()
    assert len(new_projects_soap) == len(old_projects_soap) + 1
    assert len(new_projects_db) == len(old_projects_db) + 1
    old_projects_soap.append(project)
    old_projects_db.append(project)
    assert sorted(new_projects_soap, key=Project.name_or_max) == sorted(old_projects_soap, key=Project.name_or_max)
    assert sorted(new_projects_db, key=Project.name_or_max) == sorted(old_projects_db, key=Project.name_or_max)
    #print(app.project.get_project_list())


