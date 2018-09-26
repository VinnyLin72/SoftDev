# Team Peglegs -- Jared Asch, Vincent Lin
# SoftDev pd7
# K10 -- Jinja Tuning
# 2018-09-24

from flask import Flask, render_template
from util.occupations import rand_job, parse_jobs_csv

app = Flask(__name__)

header, jobs = parse_jobs_csv()

@app.route("/")
def home(): # creates an unnecessary home page with a link to assignment
    return "<a href = occupations>Click here for occupations</a>"

@app.route("/occupations") 
def occupations(): # uses template to create the table
    return render_template('occupations.html', random = rand_job(jobs), jobs = jobs, header = header)

if __name__ == "__main__": 
    app.debug = True    # Set False for production
    app.run()
