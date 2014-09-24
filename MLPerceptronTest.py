__author__ = 'mohnish'

from numpy import *
from matplotlib.pyplot import *

color_map = {1: "ro", 2: "bo", 3: "go"}
unit_step = lambda x: 0 if x < 0 else 1
data = genfromtxt(open("multiclassdatatest.csv","r"),delimiter=",", dtype="f8")[:]

def max_value_plus_index(l):
    max_value = max(l)
    max_value_index = l.index(max_value)
    return max_value, max_value_index


weights=[[-410.,-250.],[-90.,640.],[500.,-390.]]

#weights=[[  -180.,   -100.],[   -60.,    320.],[  240.,  -220.]]

count_correct=0
count_incorrect=0

for index in xrange(len(data)):
	x = data[index][:2]
	expected_outcome = int(data[index][2])
	results=[dot(x,w) for w in weights]
	max_val,max_val_index=max_value_plus_index(results)
	print expected_outcome," ",max_val_index
	if max_val_index+1 == expected_outcome:
		count_correct=count_correct+1
	else:
		count_incorrect=count_incorrect+1

print "Correct",count_correct
print "InCorrect",count_incorrect