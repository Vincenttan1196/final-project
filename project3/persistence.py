from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from project3.models import *
from project3 import db
from sqlalchemy import desc



import shelve



users = shelve.open('user')
compproducts = shelve.open("products")
images = shelve.open("images")
catTotal = shelve.open("categoryTotal")
shoplist = shelve.open("shoppingList")

class Product:
    def __init__(self):
        self.itemid = ""
        self.name = ""
        self.picture = ""
        self.price1 = ""
        self.price2 = ""

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

    def get_price1(self):
        return self.price1

    def set_price1(self, price1):
        self.price1 = price1

    def get_price2(self):
        return self.price2

    def set_price2(self, price2):
        self.price2 = price2

    def get_itemid(self):
        return self.itemid

    def set_itemid(self, itemid):
        self.itemid = itemid


class Object(Product):
    def __init__(self):
        super().__init__()
        self.type = ""

    def set_type(self,type):
        self.type = type

    def get_type(self):
        return self.type

def add_product(product):
    compproducts[product.itemid] = product

def create_product(itemid, name, picture, price1, price2, type):
    product = Object()
    product.itemid = itemid
    product.name = name
    product.picture = picture
    product.price1 = price1
    product.price2 = price2
    product.type = type
    compproducts[itemid] = product

def get_products():
    klist = list(compproducts.keys())
    x = []
    for i in klist:
        x.append(compproducts[i])
    return x

def get_product(id):
    if id in compproducts:
        return compproducts[id]

def clear_products():
    klist = list(compproducts.keys())
    for key in klist:
        del compproducts[key]

def create_shoplist():
    if "1" not in shoplist:
        return "yes"
    else:
        return "no"

def add_shop(id):
    x = shoplist[1]
    x.append(id)

def get_shoplist():
    x = shoplist[1]
    return x

#For Bills Page (start) --------------
billinfo = shelve.open('bill')
counter = shelve.open('billcounter')
water = shelve.open('billwater')
electricity = shelve.open('billelectricity')
billothers = shelve.open('billother')
#catelist = shelve.open('categorylist')

class Bill:
    # count and index are both for tracking the bill number, it is not decided which to use yet
    def __init__(self):
        self.name = ''
        self.index = ''
        self.amount = ''
        self.due = ''
        self.category = ''


def add_totalbills(id,amount,due,name,category):
    bill = Bill()
    bill.name = name
    bill.index = id
    bill.amount = amount
    bill.due = due
    bill.category = category
    billinfo[id] = bill

def get_totalbills():
    keylist = list(billinfo.keys())
    x = []
    for i in keylist:
        x.append(billinfo[i])
    return x

def set_water(amount):
    water['x'] = amount

def set_electricity(amount):
    electricity['x'] = amount

def set_other(amount):
    billothers['x'] = amount

def set_counter(y):
    counter['x'] = y

def get_counter():
    keylist = list(counter.keys())
    if keylist == []:
        counter['x'] = 1
    count = counter['x']
    return int(count)

#--------------------------------------


#Immanuels Stuff----------------------------------------------------------------------------------





productinfo = shelve.open('productPrice')
class productInfo:
    def __init__(self):
        self.__name = ''
        self.__price = ''
        self.__index = ''
        self.__budget = ''
        self.__category = ''
        self.__food = ''
        self.__groceries = ''
        self.__entertainment = ''
        self.__luxury = ''
        self.__others = ''
        self.__addbudget = ''


    def get_name(self):
        return self.__name

    def get_addbudget(self):
        return self.__addbudget

    def get_others(self):
        return self.__others

    def get_food(self):
        return self.__food

    def get_groceries(self):
        return self.__groceries

    def get_entertainment(self):
        return self.__entertainment

    def get_luxury(self):
        return self.__luxury

    def get_category(self):
        return self.__category

    def get_budget(self):
        return self.__budget

    def get_index(self):
        return self.__index

    def get_price(self):
        return self.__price

    def set_index(self, index):
        self.__index = index

    def set_addbudget(self, addbudget):
        self.__addbudget = addbudget

    def set_others(self, others):
        self.__others = others

    def set_food(self, food):
        self.__food = food

    def set_groceries(self, groceries):
        self.__groceries = groceries

    def set_entertainment(self, entertainment):
        self.__entertainment = entertainment

    def set_luxury(self, luxury):
        self.__luxury = luxury
        
    def set_category(self, category):
        self.__category = category

    def set_budget(self, budget):
        self.__budget = budget

    def set_name(self, name):
        self.__name = name

    def set_price(self,price):
        self.__price = price


def add_productprice(productprice):
    productinfo[productprice.index] = productprice


total = shelve.open('totalprices')


def add_totalprices(totalprice):
    total['total'] = totalprice


food = shelve.open('totalfood')


def add_totalfoods(totalfood):
    food['food'] = totalfood


groceries = shelve.open('totalgrocery')


def add_groceries(totalgrocery):
    groceries['groceries'] = totalgrocery


entertainment = shelve.open('totalentertainment')


def add_entertainment(totalentertainment):
    entertainment['entertainment'] = totalentertainment


luxury = shelve.open('totalluxury')


def add_luxury(totalluxury):
    luxury['luxury'] = totalluxury


others = shelve.open('others')


def add_other(totalothers):
    others['others'] = totalothers

budget = shelve.open('budgets')

def add_budget(totalbudget):
    budget['budget'] = totalbudget

def get_productname():
    infolist = list(productinfo.keys())
    y = []
    for i in infolist:
        y.append(productinfo[i])
    return y

fambudget = shelve.open('familybudget')


class family(productInfo):
    def __init__(self, budget):
        super().__init__(budget)

    def get_budget(self):
        return self.__budget

    def set_budget(self, budget):
        self.__budget = budget


def add_familybudget(familybudget):
    fambudget[familybudget.index] = familybudget





#----------------------------------------------------------------------------------------------\




#-------------------------------------------------------------------------------------------------