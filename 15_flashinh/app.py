'''
Team Strawberry -- Vincent Lin, Clara Mohri 
SoftDev pd7  
K15 -- Oh yes, perhaps I do...
2018-10-02
'''

from flask import Flask, request, render_template, session, redirect, url_for, flash
from os import urandom

app = Flask(__name__)
app.secret_key = urandom(32)

#hard-coded username and password
users = {"person" : "pass"}

#based on whether user is known or not, displays either login or welcome page
@app.route("/")
def index():
    if "username" not in session.keys(): # checks to see if we know you
        return redirect(url_for("login")) # if not redirects you to login page
    return render_template("index.html", person = session["username"]) # if yes shows you welcome page

#processes username and password
@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html") # if redirected by index() shows the login page
    elif request.form.get("username") not in users.keys():
        flash("Error: username does not exist")
        return render_template("error.html")
    elif users[request.form.get("username")] != request.form.get("password"):
        flash("Error: password is incorrect") 
        return render_template("error.html")
    elif users[request.form.get("username")] == request.form.get("password"):
        session["username"] = request.form.get("username")
        return redirect(url_for("index"))
    return render_template("login.html")

#log out for user
@app.route("/logout", methods = ["POST"])
def logout():
    session.pop("username") #remove user
    return redirect(url_for("index")) #redirect to index function at root

if __name__ == "__main__":
    app.debug = True # False for productions
    app.run()
