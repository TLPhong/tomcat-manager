import sqlite3


class UserRepository:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        assert self.connection_string

    def _connection(self):
        return sqlite3.connect(self.connection_string)

    def get_user(self, user_name):
        """
        Find a user base on user name
        :param user_name: target user name
        :return: tuple of (username, password, note) or None
        """
        query = "SELECT (user_name, user_pass, note) FROM users WHERE user_name = :user_name"
        params = {"user_name": user_name}
        with self._connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query, params)
            found_user = cursor.fetchone()

        if found_user is not None:
            return found_user[0], found_user[1], found_user[2]
        else:
            return None

    def create_user(self, user_name, password, note):
        """
        Create an entry of user
        :param user_name: user's user name
        :param password: user's password
        :param note: note of the user
        :return: if the operation success or not
        """
        query = "INSERT INTO users (user_name, user_pass, note) VALUES (:user_name, :password, :note);"
        params = {
            "user_name": user_name,
            "password": password,
            "note": note
        }
        with self._connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query, params)
            row_effected = cursor.rowcount
        return row_effected == 1

    def edit_user(self, user_name, password, note):
        """
        Update a user
        :param user_name: user name of the user
        :param password: password for the user
        :param note: note of the user
        :return: if the operation success of not
        """
        query = "UPDATE users SET user_pass = :password, note = :note WHERE user_name = :user_name"
        params = {
            "user_name": user_name,
            "password": password,
            "note": note
        }
        with self._connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query, params)
            row_effected = cursor.rowcount
        return row_effected == 1

    def delete_user(self, user_name):
        """
        Delete a user
        :param user_name: user name of the user
        :return: if the operation success or not
        """
        query = "DELETE FROM users WHERE user_name = :user_name"
        params = {"user_name": user_name}
        with self._connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query, params)
            row_effected = cursor.rowcount
        return row_effected == 1

    def get_role(self, user_name, role_name):
        """
        Return a single mapping of user role
        :param user_name: user name of the target mapping
        :param role_name: role name of the target mapping
        :return: a tuple (user_name, role_name) of found mapping or None
        """
        query = "SELECT (user_name, role_name) FROM user_roles WHERE user_name = :user_name AND role_name = :role_name"
        params = {
            "user_name": user_name,
            "role_name": role_name
        }

        with self._connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query, params)
            found_mapping = cursor.fetchone()
        if found_mapping is not None:
            return found_mapping[0], found_mapping(1)
        else:
            return None

    def get_roles(self, user_name):
        """
        Return a list of role name for a user
        :param user_name: user name of the target user
        :return: a list of tuple (username, role name) for a user or an empty list
        """
        query = "SELECT (user_name, role_name) FROM user_roles WHERE user_name = :user_name"
        params = {"user_name": user_name}

        result = []
        with self._connection() as connection:
            cursor = connection.cursor()
            for row in cursor.execute(query, params):
                result.append(
                    (row[0], row[1])
                )
        return result

    def create_role(self, user_name, role_name):
        """
        Create a role for target user
        :param user_name: user name of the user
        :param role_name: role name of the user
        :return: if the operation success of not
        """
        query = "INSERT INTO user_roles (user_name, role_name) VALUES (:user_name, :role_name)"
        params = {
            "user_name": user_name,
            "role_name": role_name
        }
        with self._connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query, params)
            row_count = cursor.rowcount
        return row_count == 1

    def delete_role(self, user_name, role_name):
        """
        Delete a role from target user
        :param user_name:
        :param role_name:
        :return:
        """
        query = "DELETE FROM user_roles WHERE user_name = :user_name AND role_name = :role_name"
        params = {
            "user_name": user_name,
            "role_name": role_name
        }
        with self._connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query, params)
            row_count = cursor.rowcount
        return row_count == 1
