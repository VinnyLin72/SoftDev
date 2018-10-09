#The Cool Cids Club
#SofDev1 pd 7
#K17 Average
#2018-10-06

import sqlite3

DB_FILE = 'discobandit.db'
db = sqlite3.connect(DB_FILE)
c = db.cursor()

#adds to courses make note if you put in id of someone not in peeps they will be unaccounted for in the avgs table
def addToCourses(code, mark, id):
    insertion = "INSERT INTO courses VALUES({},{},{})".format("'"+ code + "'", mark, id)
    c.execute(insertion)  #add the values


def tabulate_studentInfo():
    command = "CREATE TABLE peeps_avg(id INTEGER PRIMARY KEY, average FLOAT);"
    c.execute(command)
    command = "SELECT peeps.id FROM peeps,courses WHERE peeps.id = courses.id;"
    c.execute(command)
    students_id = c.fetchall()
    students_idset = set(students_id)  #transforms list with non-unique tuples into set with unique tuples
    for tup in students_idset:
        id = tup[0]
        avg = calc_avg(id)
        insertion = "INSERT INTO peeps_avg VALUES({},{})".format(id, avg)
        c.execute(insertion)


#prints all of the students data
def display_studentsInfo():
    command = "SELECT id,average FROM peeps_avg;"
    c.execute(command)
    data = c.fetchall()
    for pair in data:
        name = get_name(pair[0])
        print("Name : {}    id: {}  average: {}\n".format(name,pair[0],pair[1]))


#using id does the avg of the student
def calc_avg(id):
     grades = get_grades(id)
     avg = 0.0
     for item in grades:
        avg+= item[0]
     avg = format(avg/len(grades), '.2f')
     return avg

#takes a students id spits out their grades
def get_grades(student_id):
    command = "SELECT mark FROM courses WHERE courses.id = {};".format(student_id)
    c.execute(command)
    student_grades = c.fetchall()
    return student_grades

def get_name(student_id):
    command = "SELECT name FROM peeps WHERE peeps.id = {};".format(student_id)
    c.execute(command)
    name = c.fetchone()
    return name[0]  #name is a tuple so return first element


tabulate_studentInfo()
display_studentsInfo()
addToCourses('calculus',85,11)

c.execute('SELECT code,mark,id FROM courses')
print(c.fetchall())

db.commit()
db.close()  #close database
