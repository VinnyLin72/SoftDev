'''
Vincent Lin
SoftDev pd7
K25 -- Getting More REST
2018-11-14
'''

from flask import Flask, render_template
import urllib, json
import ssl

app = Flask(__name__)

@app.route("/")
def index():
    context = ssl._create_unverified_context()
    x = urllib.request.urlopen("https://dog.ceo/api/breeds/image/random", context = context)
    stuff = x.read()
    data = json.loads(stuff)
    return render_template("index.html", stuff=data["message"])

if __name__ == "__main__":
    app.debug = True
    app.run()
