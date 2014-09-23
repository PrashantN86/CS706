__author__ = 'mohnish'

from matplotlib.pyplot import *
from numpy import *


unit_step = lambda x: -1 if x < 0 else 1

converter = lambda x: '*' if x == 1 else 'o'

training_data = genfromtxt(open("data\demoTrain.csv","r"),delimiter=",", dtype="f8")[:]
expected_outcomes = genfromtxt(open("data\demoTarget.csv","r"),delimiter=",", dtype="f8")[:]
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
       # w = (1/sqrt(dot(x,x)))*w

print "Training data"
for index in xrange(len(training_data)):
    print training_data[index], expected_outcomes[index]
print w


for index in xrange(len(training_data)):
        #x, expected_outcome = training_data[index]
        x = training_data[index]
        expected_outcome = expected_outcomes[index]
        plot(x[0],x[1]+10,converter(expected_outcome))

plot([0, 40], [(502/82), ((502+162*40)/82)], color='k', linestyle='-', linewidth=1)
show()