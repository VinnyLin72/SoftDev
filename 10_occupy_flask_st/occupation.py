#Team Peglegs -- Vincent Lin, Jared Asch
#SoftDev pd7
#K#10 -- Jinja Tuning
#2018 -- 09 -- 24

from flask import Flask, render_template
import csv 
from random import choice #importing all necessary functions

app = Flask(__name__)

joblist = {} #creates dictionary of jobs and percentages
header = [] #the first line of the csv file and the table heading

reader = csv.reader(open('occupations.csv', 'r'))

r = 0
for row in reader: #reads every line except the first(header) in the csv file and adds the job/percentage to the dict
    if r != 0:
        joblist[row[0]] = row[1]
    else:
        header = row #adds the header to the header list
    r += 1

def getRand(): #randomly choose a job
    keys = []
    for key in joblist.keys():
        keys.append(key) #create a list of keys(jobs)
    return choice(keys[0:-1]) #choose a random job from list


@app.route("/")
def home(): #creates an unnecessary home page with a link to assignment
	return "<a href = occupations>Click here for occupations</a>"

@app.route("/occupations") 
def occupations(): #uses template to create the table
    return render_template('occupations.html', random = getRand(), jobs = joblist, header = header)

if __name__ == "__main__":
	app.debug = True
	app.run()
