from models import Role


class User:
    def __init__(self, user_name, password):
        assert user_name
        assert password
        self.user_name = user_name
        self.password = password
        self.roles = []

    def set_roles(self, role_name_list=None):
        if role_name_list is None:
            role_name_list = []
        new_roles = []
        for role_name in role_name_list:
            new_roles.append(Role(role_name))
        self.roles = new_roles
