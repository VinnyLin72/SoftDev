#Team GreyLegs -- Alex Liu, Vincent Lin
#SoftDev pd7
#K06 -- StI/O: Divine your Destiny!
#2018-09-13

import csv
from random import choice


#instantiates the list to fill with occupations
occuList = []

#reads the csv file
reader = csv.DictReader(open('occupations.csv', 'r'))

def readList():
    for line in reader:
        i = 0
        while i < (float(line['Percentage'])*10):
            occuList.append(line['Job Class'])
            i+= 1
    #print(line)
    #removes the last line of the csv file
    for x in range(0,998):
        occuList.pop()

#adds more occupations to the occuList to increase frequencies
def fillPercent():
    for line in reader:
        i = 1
        while i < (float(line['Percentage'])*10):
            occuList.append(line['Job Class'])
            i+= 1


readList()
#print(occuList)

#testing
#import pprint
#pprint.pprint(occuList)

def randomChooser():
    print (choice(occuList))

randomChooser()
