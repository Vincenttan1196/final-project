from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "This is the homepage"

@app.route("/summary/<familyid>")
def summary(familyid):
    return render_template("summary.html", familyid = familyid)

if __name__ == "__main__":
    app.run()
