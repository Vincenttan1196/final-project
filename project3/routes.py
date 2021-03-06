import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from project3 import app, db, bcrypt, mail
from project3.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                            RequestResetForm, ResetPasswordForm)
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message
from project3.persistence import *
from project3.models import *
from project3.database import User



@app.route("/cheaper")
def cheaper():
    test = get_products()

    return render_template('comparison.html', productObjs = test)

@app.route("/comparison/<objectid>", methods=('GET', 'POST'))
def comparison(objectid):
    selectedproduct = get_product(objectid)
    # ^to display the product selected by user
    if request.method == 'POST':
        if current_user.is_authenticated:
            shoppingList = current_user.shoplist
            newList = str(shoppingList) + "," +str(objectid)
            current_user.shoplist = newList
            db.session.commit()

            keys = current_user.shoplist.split(",")
            shopList = []
            total1 = 0
            total2 = 0
            for i in keys:
                if i in compproducts:
                    shopList.append(compproducts[i])
                    total1 = total1 + float(compproducts[i].price1)
                    total2 = total2 + float(compproducts[i].price2)
            return render_template("list.html", listobj = shopList, total1 = total1, total2 = total2)
        else:
            return render_template("login.html")
    return render_template("comparison2.html", selprod = selectedproduct)

@app.route("/list")
@login_required
def list():
    if current_user.is_authenticated:
        keys = current_user.shoplist.split(",")
        shopList = []
        total1 = 0
        total2 = 0
        for i in keys:
            if i in compproducts:
                shopList.append(compproducts[i])
                total1 = total1 + float(compproducts[i].price1)
                total2 = total2 + float(compproducts[i].price2)
        return render_template("list.html", listobj=shopList, total1=total1, total2=total2)



@app.route("/admin", methods=('GET', 'POST'))
def admin():
    if request.method == 'POST':
        itemid = request.form['itemid']
        name = request.form["name"]
        picture = request.form["picture"]
        price1 = request.form["price1"]
        price2 = request.form["price2"]
        type = request.form["type"]
        create_product(itemid, name, picture, price1, price2, type)
        return render_template('admin.html')
    return render_template("admin.html")





#Jonathan's stuff -----------------------------------------------------------------------
@app.route('/schemecheck', methods=('GET', 'POST'))
def schemecheck():
    if request.method == 'POST':
        income = int(request.form['income'])
        if income >= 2000:
            return render_template('schemepage0.html')
        elif income >= 1500:
            return render_template('schemepage1.html')
        elif income >= 1000:
            return render_template('schemepage2.html')
        elif income < 1000:
            return render_template('schemepage3.html')
    return render_template('schemecheck.html')


@app.route("/bills", methods = ('GET','POST'))
@login_required
def bills():
    if request.method == 'POST':
        water = current_user.water
        electricity = current_user.electricity
        billothers = current_user.billothers
        print ('test')
        print (request.form['billcounter'])
        counter['x'] = request.form['billcounter']

        print (counter['x'])
        print (get_counter())
        for i in range(int(get_counter())):
            x = str(i + 1)
            id = x
            name = str(request.form['billname' + str(x)])
            amount = str(request.form['billamount' + str(x)])
            due = str(request.form['billdue'+str(x)])
            category = str(request.form['billcategory'+str(x)])
            add_totalbills(id,amount,due,name,category)
            #--------------------(for categories [bottom])----------
            if category == 'Water':
                water = water + int(amount)
                current_user.water = water
                db.session.commit()
            elif category == 'Electricity':
                electricity = electricity + int(amount)
                current_user.electricity = electricity
                db.session.commit()
            elif category == 'Others':
                billothers = billothers + int(amount)
                current_user.billothers = billothers
                db.session.commit()
        y = get_totalbills()
        total = 0
        for i in y:
            total += int(i.amount)
        return render_template('billsSaved.html', info = y, total = total)
    count = get_counter()
    y = get_totalbills()
    if y == []:
        add_totalbills('1','Enter the amount','Enter the due date','Enter a name','nil')
        y = get_totalbills()
    return render_template('Bills.html', count = int(count), bill = billinfo)


@app.route('/display', methods=('GET', 'POST'))
def display():
    y = get_totalbills()
    total = 0
    for i in y:
        total += int(i.amount)
    return render_template('billsSaved.html', info = y, total = total)
#------------------------------------------------------------------------------------------------

#Immanuels Stuff-------------------------------------------------------------------------------------------



@app.route("/planner", methods=('GET', 'POST'))
@login_required
def planner():
    if current_user.is_authenticated:
        if request.method == 'POST':
            total = 0
            budge = 0
            food = current_user.food
            grocery = current_user.grocery
            entertainment = current_user.entertainment
            luxury = current_user.luxury
            others = current_user.luxury
            count = int(request.form['totalitems'])
            for i in range(count):
                a = productInfo()
                a.index = str(i + 1)
                a.name = str(request.form['itemname' + str(i + 1)])
                a.price = int(request.form['itemprice' + str(i + 1)])
                a.budget = int(request.form['budget'])
                a.category = str(request.form['itemcategory' + str(i + 1)])
                total = total + int(a.price)
                budge = a.budget - total
                current_user.budget = budge
                if a.category == 'food' or a.category == 'Food':
                    food = food + int(a.price)
                    current_user.food = food
                elif a.category == 'groceries' or a.category == 'Groceries':
                    grocery = grocery + int(a.price)
                    current_user.grocery = grocery
                elif a.category == 'entertainment' or a.category == 'Entertainment':
                    entertainment = entertainment + int(a.price)
                    current_user.entertainment = entertainment
                elif a.category == 'luxury' or a.category == 'Luxury':
                    luxury = luxury + int(a.price)
                    current_user.luxury = luxury
                elif a.category == 'others' or a.category == 'Others':
                    others = others + int(a.price)
                    current_user.others = others

                bonus = total/(current_user.budget + total)

                if bonus < 0.20:
                    current_user.score = current_user.score + 2
                    db.session.commit()

                else:
                    current_user.score = current_user.score + 0
                    db.session.commit()

                add_productprice(a)
                add_totalprices(total)
                add_totalfoods(food)
                add_groceries(grocery)
                add_entertainment(entertainment)
                add_luxury(luxury)
                add_other(others)
            a = get_productname()
            return render_template("DailySummary.html", total = total, productObj = a, budget = current_user.budget, food = food, grocery = grocery, entertainment = entertainment, luxury = luxury, others = others)
        return render_template("planner.html", total='0',budget = current_user.budget)


@app.route("/DailySummary", methods=('GET', 'POST'))
def DailySummary():
    a = get_productname()
    return render_template("DailySummary.html", total = total['total'], productObj = a, food = food['food'], grocery = groceries['groceries'], entertainment = entertainment['entertainment'], luxury = luxury['luxury'], others = others['others'])



@app.route("/summary")
@login_required
def nosummary():
    if current_user.is_authenticated:
        thing = []
        highest = 0
        things = {"Food": current_user.food,
                   "Groceries": current_user.grocery,
                   "Entertainment": current_user.entertainment,
                   "Luxury":current_user.luxury,
                  "Others": current_user.others,
                  "Water": current_user.water,
                  "Electricity": current_user.electricity}
        for i in things:
            thing.append(things[i])
        highest = max(thing)


        totalspent = current_user.food + current_user.grocery + current_user.entertainment + current_user.luxury + current_user.others
        save = round((current_user.budget - totalspent)/current_user.budget*100, 2)
        lost = round(100 - save, 2)
        percentage = round((highest / current_user.budget) * 100, 2)
        return render_template("summary.html", familyid = current_user.username, highest = highest, save = save, lost = lost, percentage = percentage)



#-------------------------------------------------------------------------------------------------




#Michaels stuff






@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/pics', picture_fn)

    output_size = (170, 170)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.password.data = current_user.password

    image_file = url_for('static', filename='pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='project3nyp@gmail.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)


@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html', title='Reset Password', form=form)


@app.route('/ranking')
def ranking():
    score = User.query.order_by(User.score.desc()).all()
    return render_template("ranking.html", score=score)


@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/consult')
def consult():
    return render_template('consult.html')

#-------------------------------------------------------------------------------------------