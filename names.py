from mysqlconnection import connectToMySQL

class Name:
    def __init__ (self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data ["updated_at"]
    @classmethod
    def get_names(cls):
        query = "SELECT * FROM users ORDER BY id"
        db_names = connectToMySQL("users_schema").query_db(query)
        names = []
        for data in db_names:
            names.append(Name(data))
        return names

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES(%(first_name)s, %(last_name)s, %(email)s)"
        return connectToMySQL("users_schema").query_db(query, data)