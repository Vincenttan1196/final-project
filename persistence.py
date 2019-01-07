import shelve
import uuid
from datetime import date
# today = str(date.today())
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import app
from flask_wtf import *
from wtforms import *
from wtforms.validators import *


def get_reset_token(self, expires_sec=1800):
    s = Serializer(app.config['SECRET_KEY'], expires_sec)
    return s.dumps({'user_id': self.id}).decode('utf-8')




def  validate_email(self,email):
    user = User.query.filter_by(email=email.data).first()
    if user:
        raise ValidationError('No account with that email')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')


users = shelve.open('user')
compproducts = shelve.open("products")
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

class Products:
    def __init__(self, itemid):
        self.itemid = itemid
        self.name = ""
        self.picture = ""
        self.price = ""

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_picture(self):
        return self.picture

    def set_picture(self, picture):
        self.picture = picture

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_itemid(self):
        return self.itemid

    def set_itemid(self, itemid):
        self.itemid = itemid

images["imagesProducts"] = ["attackLiqDet.jpg", "darlieToothpaste.JPG", "knifeCookingOil.jpg"]

def add_product(itemid, name, picture, price):
    products = Products(1)
    products.itemid = itemid
    products.name = name
    products.picture = picture
    products.price = price
    compproducts[itemid] = products

def get_products(itemid):
    if itemid in compproducts:
        return compproducts[itemid]

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


def check_user(username):
        klist = list(users.keys())
        for key in klist:
            user = users[key]
            print(user.get_username(), username)
            if user.get_username() == username:
                return True
            return False


#For Bills Page (start) --------------
bills = shelve.open('bill')

def add_amount(x,amount,due):
    bills[x] = [amount,due]

def get_amount(x):
    return bills[x]
#--------------------------------------

planner = shelve.open('planner')


def add_item(x,name,price,category):
    planner[x] = [name,price,category]

def get_item(x):
    return planner[x]
