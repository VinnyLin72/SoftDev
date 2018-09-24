#Team Peglegs -- Vincent Lin, Jared Asch
#SoftDev pd7
#K#10 -- Jinja Tuning
#2018 -- 09 -- 24

from flask import Flask, render_template
import csv
from random import choice

app = Flask(__name__)

reader = csv.reader(open('occupations.csv', 'r'))
joblist = {}
header = []

r = 0

for row in reader:
    if r != 0:
        joblist[row[0]] = row[1]
    else:
        header = row
    r += 1
#print(joblist.keys())
keys = []
for key in joblist.keys():
    keys.append(key)

random = choice(keys[0:-1])


@app.route("/")
def home():
	return "<a href = occupations>Occupations</a>"

@app.route("/occupations")
def occupations():
    return render_template('occupations.html', random = random, jobs = joblist, header = header)

if __name__ == "__main__":
	app.debug = True
	app.run()
