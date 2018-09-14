#Team GreyLegs -- Vincent Lin, Alex Liu
#SoftDev pd7
#K06 -- StI/O: Divine your Destiny!
#2018-09-13

from csv import reader
from random import randint

d = {}
reader = reader(open('occupations.csv', 'r')) #reads the csv file 
r = 0
for row in reader: #converts the csv file to a dictionary
    #print(row)
    if r != 0: #so the first row isn't included 
        d[float(row[1])] = row[0] #float to make sure percentages are stored as numbers
    r += 1

#print(d)

d.pop(99.8) #remove the total

#print(d) #testing purposes

keys = d.keys()

keylist = [] 
keysum = 0.0
for x in keys: #creating a list of keys
    keylist.append(x)
    keysum += x #finding the sum of the keys

#print(keysum)
#print(keys) #testing perposes

def randOcc():
    ri = float(randint(0, int(keysum))) #choose a random float
    for x in keylist:
        if ri > x:
            #print('ri') #testing
            #print(ri)
            ri -= x #subtract until float becomes less than or equal to a key
        else:
            #print('x')
            #print(x)
            return d[x] #returns value of first valid key

print(randOcc())
