import shelve

class User:
    def __init__(self):
        self.username = ''
        self.password = ''

users = shelve.open('user')

def clear_user():
    klist = list(users.keys())
    for key in klist:
        del users[key]

def get_users():
    user_list = []
    klist = list(users.keys())
    for key in klist:
        user_list.append(users[key])
    return user_list

def init_users():
    clear_user()
    for i in range(5):
        create_user('user'+str(i), 'pass'+str(i))

def get_user(username, password):
    if username in users:
        user = users[username]
        if  user.password == password:
            return user
    return None

def create_user(username, password):
    u = User()
    u.username = username
    u.password = password
    users[username] = u


##test##

class scores(User):
    def __init__(self, username, score):
        super().__init__()
        self.__username = username
        self.__score = score
        super(score, self).__init__()

    def get_username(self):
        return self.__username

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if self.__username == '':
            return
        self.__score = score