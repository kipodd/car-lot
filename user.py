from file_handler import FileHandler


class User:
    def user_auth(self, name, password, users_csv):
        if type(name) != str or type(password) != str or type(users_csv) != str:
            raise ValueError("Input should be string.")

        reader = FileHandler(users_csv)
        users = reader.get_csv_data()

        for user in users:
            if user["name"] == name and user["password"] == password:
                return user["role"]
        return False
