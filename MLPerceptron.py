__author__ = 'mohnish'

from numpy import *
from matplotlib.pyplot import *

color_map = {1: "ro", 2: "bo", 3: "go"}
unit_step = lambda x: 0 if x < 0 else 1
data = genfromtxt(open("multiclassdata.csv","r"),delimiter=",", dtype="f8")[:]

def max_value_plus_index(l):
    max_value = max(l)
    max_value_index = l.index(max_value)
    return max_value, max_value_index


weights = [[0,0,0],[0,0,0],[0,0,1]]
print weights
recalculate = True
round_count = 1
while recalculate:
    recalculate = False
    recalculate_count = 0
    for index in xrange(len(data)):
        x = data[index][:2]
        x = append(x, 1)
        expected_outcome = data[index][2]
        #print "x = ", x
        result = [dot(x, w) for w in weights]
        print "result= ", result
        max_val, max_val_index = max_value_plus_index(result)
        #print max_val, max_val_index

        print expected_outcome, max_val_index+1
        if expected_outcome != max_val_index+1:
            weights[int(expected_outcome)-1] += x
            weights[int(max_val_index)] -= x
            recalculate = True
            print "recalculate"
            recalculate_count += 1
    print "Recalculate_count", recalculate_count
    recalculate_count = 0

print "weights:"
print weights

x_sum=y_sum=0.
count=0
for x in data:
       # print x[0],x[1],color_map[x[2]]
		x_sum=x_sum+x[0]
		y_sum=y_sum+x[1]
		count=count+1

x_shift=x_sum/count
y_shift=y_sum/count

for x in data:
	plot(x[0]-x_shift,x[1]-y_shift,color_map[x[2]])

#x1,x2,n,m,b=-100,100.,10,-2.,-156.23
#x=r_[x1:x2:n*1j]
#plot(x,m*x+b, color='r')

#x1,x2,n,m,b=-100.,100.,10,13./12.,-2803./240.
#x=r_[x1:x2:n*1j]
#plot(x,m*x+b, color='b')

#x1,x2,n,m,b=-100.,100.,10,6./34.,12817./340.
#x=r_[x1:x2:n*1j]
#plot(x,m*x+b, color='g')

plot([0,weights[0][0]], [0,weights[0][1]], color='r', linestyle='-', linewidth=1)
plot([0,weights[1][0]], [0,weights[1][1]], color='b', linestyle='-', linewidth=1)
plot([0,weights[2][0]], [0,weights[2][1]], color='g', linestyle='-', linewidth=1)

show()