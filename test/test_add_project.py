from model.project import Project

def test_add_project(app, db, json_projects):
    project = json_projects
    old_contacts = db.get_project_list()
    app.project.create(project)
    new_contacts = db.get_project_list()
    assert len(new_contacts) == len(old_contacts) + 1
    old_contacts.append(project)
    assert sorted(new_contacts, key=Project.name_or_max) == sorted(old_contacts, key=Project.name_or_max)
    #print(app.project.get_project_list())


