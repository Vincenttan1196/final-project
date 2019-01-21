from flask import Flask
from flask_sqlalchemy import SQLAlchemy



import shelve



users = shelve.open('user')
compproducts = shelve.open("products")
images = shelve.open("images")


class Product:
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



def add_product(product):
    compproducts[product.itemid] = product

def create_product(itemid, name, price):
    product = Product()
    product.itemid = itemid
    product.name = name
    product.price = price
    compproducts[itemid] = product

def get_products():
    klist = list(compproducts.keys())
    x = []
    for i in klist:
        x.append(compproducts[i])
    return x

def clear_product(id):
    del compproducts[id]


#For Bills Page (start) --------------
billinfo = shelve.open('bill')


class Bill:
    count = 0

    # count and index are both for tracking the bill number, it is not decided which to use yet
    def __init__(self):
        self.index = ''
        self.amount = ''
        self.due = ''

    def set_amount(self, amount):
        self.amount = amount

    def set_due(self, due):
        self.due = due

def add_totalbills(id,amount,due):
    bill = Bill()
    bill.id = id
    bill.amount = amount
    bill.due = due
    billinfo[id] = bill

def get_totalbills():
    keylist = list(billinfo.keys())
    x = []
    for i in keylist:
        x.append(billinfo[i])
    return x

#--------------------------------------


#Immanuels Stuff----------------------------------------------------------------------------------

productinfo = shelve.open('productPrice')
class productInfo:
    def __init__(self):
        self.name = ''
        self.price = ''
        self.index = ''
        self.indivprice = ''

    def get_name(self):
        return self.name

    def get_index(self):
        return self.index

    def get_price(self):
        return self.price

    def get_indivprice(self):
        return self.indivprice

    def set_index(self, index):
        self.index = index

    def set_indivprice(self, indivprice):
        self.indivprice = indivprice

    def set_name(self, name):
        self.name = name

    def set_price(self,price):
        self.price = price


def add_productprice(productprice):
    productinfo[productprice.index] = productprice


total = shelve.open('totalprices')

def add_totalprices(totalprice):
    total['total'] = totalprice


def get_productname():
    infolist = list(productinfo.keys())
    y = []
    for i in infolist:
        y.append(productinfo[i])
    return y

#----------------------------------------------------------------------------------------------\

#Michael stuff

















#-------------------------------------------------------------------------------------------------