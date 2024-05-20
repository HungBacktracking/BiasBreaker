from database.database import db
from bson import ObjectId

users = db["users"]


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    @staticmethod
    def find_one(email):
        return users.find_one({"email": email})
    
    @staticmethod
    def find_one_by_id(id):
        return users.find_one({"_id": ObjectId(id)})

    @staticmethod
    def create(email, password):
        user = User(email, password)
        users.insert_one(user.to_dict())
        return user

    @staticmethod
    def delete(email):
        users.delete_one({"email": email})

    @staticmethod
    def delete_by_id(id):
        users.delete_one({"_id": ObjectId(id)})

    @staticmethod
    def update(email, password):
        users.update_one({"email": email}, {"$set": {"password": password}})

    @staticmethod
    def update_by_id(id, password):
        users.update_one({"_id": ObjectId(id)}, {"$set": {"password": password}})

    @staticmethod
    def checkExists(email):
        return User.find_one(email) is not None

    @staticmethod
    def validate(email, password):
        user = User.find_one(email)
        if user is None:
            return False
        return user["password"] == password

    def to_dict(self):
        return {"email": self.email, "password": self.password}
