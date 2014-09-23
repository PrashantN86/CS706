from numpy import array, dot, random
#2 input OR gate
#this rounds the calculated dot product to appropriate label
unit_step = lambda x:0 if x < 0 else 1
#training data set with 3rd attribute being d+1 th dimension
#the data is in the form (array x,y) where x is the input vector and y is the expected outcome
#example: x = array([0, 0, 1]) , y = 0
training_data = [(array([0, 0, 1]), 1), (array([0, 1, 1]), 1), (array([1, 0, 1]), 0), (array([1, 1, 1]), 0), ]
#weight vector
w = [0, 0, 0]
print "w = ", w
errors = []
n = 0
recalculate = True
while recalculate:
    recalculate = False
    for i in xrange(len(training_data)):
        n += 1
        x, expected = training_data[i]
        result = dot(w, x)
        print result, expected
        error = expected - unit_step(result)
        #if product does not match the expected label
        if error != 0:
            recalculate = True
            errors.append(error)
        w += error * x
for x, _ in training_data:
    result = dot(x, w)
    print("{}: {} -> {}".format(x[:2], result, unit_step(result)))
print "Number of iterations : ", n
print w