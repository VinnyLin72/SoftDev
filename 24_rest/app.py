'''

'''

from flask import Flask, render_template
import urllib, json
import ssl

app = Flask(__name__)

@app.route("/")
def index():
    context = ssl._create_unverified_context()
    x = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=2evCliypb1mU9AQ6tJvFH6503oS0e4lJMArEIq7p", context = context)
    stuff = x.read()
    data = json.loads(stuff)
    return render_template("index.html", stuff=data["url"], data=data["explanation"])

if __name__ == "__main__":
    app.debug = True
    app.run()
