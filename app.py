from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "This is the homepage"

@app.route("/test")
def test():
    return "<h1> Hello World this is vincent </h1>"

if __name__ == "__main__":
    app.run()
