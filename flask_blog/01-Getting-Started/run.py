from flask import Flask, redirect , url_for
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"


@app.route("/about")
def about():
    return "<h1>About Page</h1>"

@app.route("/<name>")
def info(name):
    return f"<h1> Hello {name:#^50} <h1>"

@app.route("/admin") # access /admin redirect to /home
def user():
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)