import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from project3 import app, db, bcrypt, mail
from project3.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                            RequestResetForm, ResetPasswordForm)
from project3.models import User
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message
from project3.persistence import *


@app.route("/summary/<familyid>")
def summary(familyid):
    return render_template("summary.html", familyid = familyid)


@app.route("/cheaper")
def cheaper():
    imageList = get_imagesproduct()
    return render_template("comparison.html", imageList = imageList)


@app.route("/admin", methods=('GET', 'POST'))
def admin():
    if request.method == 'POST':
        name = request.form["name"]
        picture = request.form["picture"]
        price = request.form["price"]
    return render_template("admin.html")



@app.route('/ranking')
def ranking():
    return render_template("ranking.html")


#Testing php#
@app.route('/weekly')
def weekly():
    return render_template("weekly.html")


@app.route('/monthly')
def monthly():
    return render_template("monthly.html")


@app.route('/yearly')
def yearly():
    return render_template("yearly.html")


@app.route('/feedback')
def feedback():
    return render_template('feedback.html')


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
def bills():
    if request.method == 'POST':
        for i in range(3):
            x = str(i + 1)
            amount = str(request.form['amount'+str(x)])
            due = str(request.form['due'+str(x)])
            add_amount(x,amount,due)
        return render_template('billsSaved.html', amount1 = get_amount('1')[0], due1= get_amount('1')[1], amount2 ='')

    return render_template('Bills.html')


@app.route('/display', methods=('GET', 'POST'))
def display():
    return render_template('billsSaved.html', amount1=get_amount('1')[0], due1=get_amount('1')[1], amount2='')
#------------------------------------------------------------------------------------------------



@app.route("/planner", methods=('GET', 'POST'))
def planner():
    if request.method == 'POST':
        total = 0
        for i in range(3):
            x = str(i + 1)
            itemname = str(request.form['itemname'+str(x)])
            itemprice = int(request.form['itemprice'+str(x)])
            itemcategory = str(request.form['category'+str(x)])
            total = total + itemprice
        return render_template("DailySummary.html", total = total)
    return render_template("planner.html", total='0')




#testing







posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


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
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
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
