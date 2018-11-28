import random
from model.project import Project


def test_delete_project(app, db):
    if len(app.soap.get_project_list()) == 0:
        app.project.create(Project(name="delete_project"))
    old_projects_soap = app.soap.get_project_list()
    old_projects_db = db.get_project_list()
    project = random.choice(old_projects_db)
    app.project.delete_project_by_id(project.id)
    new_projects_db = db.get_project_list()
    new_projects_soap = app.soap.get_project_list()
    assert len(new_projects_db) == len(old_projects_db) - 1
    assert len(new_projects_soap) == len(old_projects_soap) - 1