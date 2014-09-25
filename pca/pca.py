import csv
import numpy
from operator import add
from numpy import linalg as LA

reader=csv.reader(open("test.tes","rb"),delimiter=',')
x=list(reader)

def myFloat(myList):
	return map(float, myList)

init_input=map(myFloat, x)

average=[0.]*64

#remove final coloumn
for row in init_input:
	del row[-1]
	average=map(add, average, row)

average=[value/1797 for value in average]

init_input=numpy.asarray(init_input)
average=numpy.asarray(average)

#Subtract mean
for i in xrange(len(init_input)):
	init_input[i]=numpy.subtract(init_input[i],average)


covar=numpy.cov(init_input)
w, v = LA.eig(covar)

#print init_input[1796]
