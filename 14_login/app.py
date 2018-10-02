#Team Strawberry -- Vincent Lin, Clara Mohri
#SoftDev pd7
#K14 -- Do I Know You?
#2018-10-01

from flask import Flask, request, render_template, session, redirect, url_for
from os import urandom

app = Flask(__name__)
app.secret_key = urandom(32)

users = {"person" : "pass"}

@app.route("/")
def index():
    if "username" not in session.keys(): # checks to see if we know you
        return redirect(url_for("login")) # if not redirects you to login page
    return render_template("index.html", person = session["username"]) # if yes shows you welcome page

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html") # if redirected by index() shows the login page
    elif request.form.get("username") not in users.keys():
        return render_template("error.html", error = "your username does not exist!")
    elif users[request.form.get("username")] != request.form.get("password"):
        return render_template("error.html", error = "your password is incorrect!")
    elif users[request.form.get("username")] == request.form.get("password"):
        session["username"] = request.form.get("username")
        return redirect(url_for("index"))
    return render_template("login.html")


@app.route("/logout", methods = ["POST"])
def logout():
    session.pop("username")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.debug = True # False for productions
    app.run()
