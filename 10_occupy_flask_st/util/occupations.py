import csv 
from random import random   # importing all necessary functions

def parse_jobs_csv():
    jobs_dict = {}    # creates dictionary of jobs and percentages
    header = [] # the first line of the csv file and the table heading
    reader = csv.reader(open('data/occupations.csv', 'r'))
    r = 0
    for row in reader:  # reads every line except the first(header) in the csv file and adds the job/percentage to the dict
        if r != 0:
           jobs_dict[row[0]] = float(row[1])
        else:
            header = row    # adds the header to the header list
        r += 1
    return header, jobs_dict

def rand_job(occupations):
    percents = list(occupations.values())
    occs = list(occupations.keys())
    rand = random() * 99.8
    percentTot = percents[0];
    index = 0;
    while(percentTot < rand):
        index += 1
        percentTot += percents[index]
    return (occs[index])   # choose a random job from list