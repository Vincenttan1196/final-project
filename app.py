from flask import Flask, render_template
app = Flask(__name__)

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev'
)


@app.route("/")
def index():
    return "This is the homepage"


@app.route("/summary/<familyid>")
def summary(familyid):
    return render_template("summary.html", familyid = familyid)


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/signup')
def signup():
    return render_template('signup.html')


if __name__ == "__main__":
    app.run()