import random
from model.project import Project


def test_delete_project(app, db):
    if len(db.get_project_list()) == 0:
        app.project.create(Project(name="delete_project"))
    old_contacts = db.get_project_list()
    projects = db.get_project_list()
    project = random.choice(projects)
    app.project.delete_project_by_id(project.id)
    new_contacts = db.get_project_list()
    assert len(new_contacts) == len(old_contacts) - 1