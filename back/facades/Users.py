import logging

from models import User, Application


class Users:
    def __init__(self, config):
        from facades.UserRepository import UserRepository
        self.user_repo = UserRepository(config)

    def list(self):
        """
        Get a list of user
        :return: a list of user | empty list if none found | None if can't fetch
        """
        logging.debug("Fetching users")
        result_users = None
        try:
            result_users = []
            for (username, password, note) in self.user_repo.list_user():
                user = User(
                    user_name=username,
                    password=password,
                    note=note
                )
                apps = []
                for (_, role_name) in self.user_repo.get_roles(user.user_name):
                    apps.append(Application(app_name=role_name))
                user.set_apps(apps)
                result_users.append(user)
        except Exception as e:
            logging.exception("Fail to list user", exc_info=e)
        return result_users

