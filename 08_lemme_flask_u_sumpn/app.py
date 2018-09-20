#Vincent Lin
#SoftDev1 pd7
#K08 -- Fill Yer Flask
#2018--09--19

from flask import Flask
App = Flask(__name__)

@app.route("/route")
def route1():
	return "route number A"

@app.route("/route")
def route2():
	return "route letter 2"

@app.route("/route")
def route3():
	return "3st route"

if __name__ = "__main__":
	app.debug = True
	app.run()
