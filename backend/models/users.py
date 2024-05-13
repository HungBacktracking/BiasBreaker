from database import db

users = db['users']
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    @staticmethod
    def find_one(email):
        return users.find_one({'email': email})

    @staticmethod
    def create(email, password):
        user = User(email, password)
        users.insert_one(user.__dict__)
        return user

    @staticmethod
    def delete(email):
        users.delete_one({'email': email})

    @staticmethod
    def update(email, password):
        users.update_one({'email': email}, {'$set': {'password': password}})

    @staticmethod
    def validate(email, password):
        user = User.find_one(email)
        if user is None:
            return False
        return user['password'] == password

    def __dict__(self):
        return {
            'email': self.email,
            'password': self.password
        }