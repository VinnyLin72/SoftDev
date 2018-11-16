'''
Vincent Lin
SoftDev pd7
K26 -- Getting More REST
2018-11-15
'''

from flask import Flask, render_template
import urllib, json
import ssl

app = Flask(__name__)

@app.route("/")
def index():
    context = ssl._create_unverified_context()

    fc_url = urllib.request.urlopen("https://api.darksky.net/forecast/2ce59e54cdf85e1d6c238ea2f6e53c06/40.718,-74.014", context = context)
    fc_api = fc_url.read()
    fc_data = json.loads(fc_api)

    cn_url = urllib.request.urlopen("http://api.icndb.com/jokes/random", context = context)
    cn_api = cn_url.read()
    cn_data = json.loads(cn_api)

    poem_url = urllib.request.urlopen("https://www.poemist.com/api/v1/randompoems", context = context)
    poem_api = poem_url.read()
    poem_data = json.loads(poem_api)
    
    return render_template("index.html", fc_stuff=fc_data["currently"], cn_stuff=cn_data["value"]["joke"], poem_title=poem_data[0]["title"], poem_content=poem_data[0]["content"])

if __name__ == "__main__":
    app.debug = True
    app.run()
