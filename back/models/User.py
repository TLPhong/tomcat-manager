from models import Application


class User:
    def __init__(self, user_name, password, note=""):
        assert user_name
        assert password
        self.user_name = user_name
        self.password = password
        self.note = note
        self.applications = []

    def set_apps(self, app_list=None):
        if app_list is None:
            app_list = []
        new_apps = []
        for app in app_list:
            new_apps.append(Application(app))
        self.applications = new_apps

    @property
    def is_admin(self):
        return False

    @is_admin.setter
    def is_admin(self, is_admin):
        # Do nothing
        pass


    def serialize(self):
        return {
            "username": self.user_name,
            "password": self.password,
            "isAdmin": self.is_admin,
            "note": self.note,
            "apps": self.applications
        }
