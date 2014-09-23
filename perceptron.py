from numpy import genfromtxt, savetxt
from sklearn import linear_model
from sklearn.linear_model.perceptron import Perceptron
import matplotlib.pyplot as plt

def main():
    #create the training & test sets, skipping the header row with [1:]



    dataset_T = genfromtxt(open('Data/demoTrain.csv','r'), delimiter=',', dtype='f8')[:]    
    
    dataset_R = genfromtxt(open('Data/demoTarget.csv','r'), delimiter=',', dtype='f8')[:]
    
    dataset_v = genfromtxt(open('Data/demoTest.csv','r'), delimiter=',', dtype='f8')[:]
    
    trueData = genfromtxt(open('Data/validate.csv','r'), delimiter=',', dtype='f8')[:]
    
    target = [x for x in dataset_R]
    train = [x[:] for x in dataset_T]
    validate = [x[:] for x in dataset_v]
    y = [x for x in trueData]
    
    
    test = genfromtxt(open('Data/demoTest.csv','r'), delimiter=',', dtype='f8')[:]
     
    
     
    per = Perceptron(n_iter=2, shuffle=True)
    per.fit(train, target)

   
    
    #val = per.decision_function(validate)
    
    val = per.predict(validate)
    score = per.score(validate, y)
    
    print str(score) +"\n"
    
    for v in val: 
        print v
    
    a= per.fit_transform(train,target)
    print a


if __name__=="__main__":
    main()