from flask import *
import functools
from persistence import *

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev'
)

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session['id'] is None:
            return redirect(url_for('login'))
        return view(**kwargs)
    return wrapped_view


@app.route('/init')
def init():
    init_db()
    return 'db initialised'

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

#@app.route('/signup')
#def signup():
    #return render_template("signup.html")


@app.route('/forgot_password')
def forgot_password():
    return render_template("forgot_password.html")


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


@app.route('/email')
def email():
    return render_template('email.html')



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


''' The challenge begins '''


@app.route("/")
def starter():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            user = get_user(username, password)
            if user is None:
                error = 'Wrong username and password'
            else:
                session['id'] = user.get_id()
                session['user_name'] = user.get_username()
                return redirect(url_for('ranking'))
        flash(error)
    return render_template('login.html')


@app.route('/login',  methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            user = get_user(username, password)
            if user is None:
                error = 'Wrong username and password'
            else:
                session['id'] = user.get_id()
                session['user_name'] = user.get_username()
                return redirect(url_for('ranking'))
        flash(error)
    return render_template('login.html')


@app.route('/signup', methods=('GET', 'POST'))
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            validation = check_user(username)
            if validation is False:
                error = 'Username already taken,choose another one'
            else:
                create_user(username, password)
                return redirect(url_for('login'))
        flash(error)
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('ranking'))



if __name__ == "__main__":
    app.run()