import random

def test_delete_project(app, db):
    old_contacts = db.get_project_list()
    projects = db.get_project_list()
    project = random.choice(projects)
    app.project.delete_project_by_id(project.id)
    new_contacts = db.get_project_list()
    assert len(new_contacts) == len(old_contacts) - 1