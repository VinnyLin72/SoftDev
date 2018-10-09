#Peter Cwalina, Jabir Chowdhury
#SoftDev1 pd7
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()


def read_csv():
        command = "CREATE TABLE courses (code TEXT,mark INTEGER, id INTEGER);"
        c.execute(command)

        with open('data/courses.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                insertion = "INSERT INTO courses VALUES({},{},{})".format("'"+ row['code'] + "'",row['mark'],row['id'])
                c.execute(insertion)

        command = "CREATE TABLE peeps (name TEXT,age INTEGER, id INTEGER PRIMARY KEY);"
        c.execute(command)

        with open('data/peeps.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                insertion = "INSERT INTO peeps VALUES({},{},{})".format("'"+ row['name'] + "'",row['age'], row['id'])
                c.execute(insertion)

read_csv()

db.commit()
db.close()  #close database
