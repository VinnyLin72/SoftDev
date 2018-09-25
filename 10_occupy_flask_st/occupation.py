#Team Peglegs -- Vincent Lin, Jared Asch
# SoftDev pd7
# K10 -- Jinja Tuning
# 2018-09-24

from flask import Flask, render_template
import csv 
from random import choice   # importing all necessary functions

app = Flask(__name__)

def parse_jobs_csv():
    jobs_dict = {}    # creates dictionary of jobs and percentages
    header = [] # the first line of the csv file and the table heading
    reader = csv.reader(open('data/occupations.csv', 'r'))
    r = 0
    for row in reader:  # reads every line except the first(header) in the csv file and adds the job/percentage to the dict
        if r != 0:
           jobs_dict[row[0]] = row[1]
        else:
            header = row    # adds the header to the header list
        r += 1
    return header, jobs_dict

def get_rand(jobs):  # randomly choose a job
    keys = []
    for key in jobs.keys():
        keys.append(key)    # create a list of keys(jobs)
    return choice(keys[0:-1])   # choose a random job from list

@app.route("/")
def home(): # creates an unnecessary home page with a link to assignment
    return "<a href = occupations>Click here for occupations</a>"

@app.route("/occupations") 
def occupations(): # uses template to create the table
    header, jobs = parse_jobs_csv()
    return render_template('occupations.html', random = get_rand(jobs), jobs = jobs, header = header)

if __name__ == "__main__": 
    app.debug = True    # Set False for production
    app.run()
