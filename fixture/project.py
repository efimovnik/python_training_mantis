from model.project import Project
from selenium.webdriver.support.ui import Select


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        # go to manage page
        if not (wd.current_url.endswith("manage_overview_page.php")):
            wd.find_element_by_link_text("Manage").click()
        # go to projects page
        if not (wd.current_url.endswith("manage_proj_page.php")):
            wd.find_element_by_link_text("Manage Projects").click()

    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        # init project creation
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        # submit project creation
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.open_projects_page()
        self.project_cache = None

    def fill_project_form(self, project):
        self.change_field_name("name", project.name)
        self.select_status("status", project.status)
        self.select_status("view_state", project.view_status)
        self.change_field_name("description", project.description)

    def select_status(self, field_status_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_status_name).click()
            Select(wd.find_element_by_name(field_status_name)).select_by_visible_text(text)
            wd.find_element_by_name(field_status_name).click()

    def change_field_name(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    project_cache = None

