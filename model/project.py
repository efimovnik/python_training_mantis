from sys import maxsize


class Project:

    def __init__(self, id=None, name=None, status=None, inherit_global=None, enabled=None, view_status=None, description=None):
        self.name = name
        self.id = id
        self.status = status
        self.inherit_global = inherit_global
        self.enabled = enabled
        self.view_status = view_status
        self.description = description

    def __repr__(self):
        return "%s;%s;%s;%s;%s;%s" % (self.name, self.status, self.inherit_global, self.enabled, self.view_status, self.description)

    def __eq__(self, other):
        return self.name == other.name

    def name_or_max(self):
        if self.name:
            return self.name
        else:
            return maxsize
