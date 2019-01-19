import shelve
from project3.models import User
from project3.models import db



users = shelve.open('user')
compproducts = shelve.open("products")
images = shelve.open("images")


class Products:
    def __init__(self):
        self.itemid = ""
        self.name = ""
        self.picture = ""
        self.price = ""

    def get_id(self):
        return self.itemid

    def set_id(self, itemid):
        self.itemid = itemid

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


def add_product(product):
    compproducts[product.itemid] = product


def get_products(itemid):
    if itemid in compproducts:
        return compproducts[itemid]


def get_imagesproduct():
    return images["imagesProducts"]



#For Bills Page (start) --------------
bills = shelve.open('bill')

def add_amount(x,amount,due):
    bills[x] = [amount,due]

def get_amount(x):
    return bills[x]
#--------------------------------------