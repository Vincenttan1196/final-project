import shelve
import uuid
from datetime import date
# today = str(date.today())

users = shelve.open('user')
images = shelve.open("images")

class User:
    def __init__(self, id):
        self.__id = id
        self.__username = ''
        self.__password = ''

    def get_id(self):
        return self.__id

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

images["imagesProducts"] = ["attackLiqDet.jpg", "darlieToothpaste.JPG"]

def get_imagesproduct():
    return images["imagesProducts"]

def create_user(username, password):
    id = str(uuid.uuid4())
    user = User(id)
    user.set_username(username)
    user.set_password(password)
    users[id] = user


def get_user(username, password):
    klist = list(users.keys())
    for key in klist:
        user = users[key]
        print(user.get_username(), username, user.get_password(), password)
        if user.get_username() == username and user.get_password() == password:
            return user
    return None


def update_user(id, user):
    users[id] = user
    return users[id]


def clear_user():
    klist = list(users.keys())
    for key in klist:
        del users[key]

def add_user(user):
    users[user.get_id()] = user

def init_db():
    clear_user()
    for i in range(5):
        create_user('user'+str(i), 'pass'+str(i))
