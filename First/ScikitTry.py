__author__ = 'mohnish'
from numpy import *

unit_step = lambda x: -1 if x < 0 else 1
training_data = genfromtxt(open("demoTrain.csv","r"),delimiter=",", dtype="f8")[:]
expected_outcomes = genfromtxt(open("demoTarget.csv","r"),delimiter=",", dtype="f8")[:]
#print training_data

w = [0, 0]
recalculate = True

while recalculate:
    recalculate = False
    for index in xrange(len(training_data)):
        #x, expected_outcome = training_data[index]
        x = training_data[index]
        expected_outcome = expected_outcomes[index]
        print x
        result = dot(w, x)
        print result, expected_outcome
        error = expected_outcome - unit_step(result)
        if error != 0:
            recalculate = True
        w += error*x

print "Training data"
for index in xrange(len(training_data)):
    print training_data[index], expected_outcomes[index]
print w