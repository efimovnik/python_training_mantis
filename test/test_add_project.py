
from model.project import Project

def test_add_project(app):
    app.project.create(Project(name="name", status="release", view_status="public", description="description"))


