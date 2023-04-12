# Advanced level
'''
You are given an array x_train with multiple input vectors (the "training data") and another array x_test with one more input 
vector (the "test data"). Find the vector in x_train that is most similar to the vector in x_test. In other words, find the nearest neighbor of the test data point x_test.

The code template gives the function dist to calculate the distance between any two vectors. What you need to add is the 
implementation of the function nearest that takes the arrays x_train and x_test and prints the index (as an integer between 0, ..., len(x_train)-1) of the nearest neighbor.
'''
import numpy as np

x_train = np.random.rand(10, 3)   # generate 10 random vectors of dimension 3
x_test = np.random.rand(3)        # generate one more random vector of the same dimension

def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)
    
def nearest(x_train, x_test):
    nearest = -1
    min_distance = np.Inf
    # add a loop here that goes through all the vectors in x_train and finds the one that
    # is nearest to x_test. return the index (between 0, ..., len(x_train)-1) of the nearest
    # neighbor
    for index, xt in enumerate(x_train):
        d = dist(xt, x_test)
        if d < min_distance:
            min_distance = d
            nearest = index
    print(nearest)

nearest(x_train, x_test)

'''
Here is a short piece of code, using the same cabin pricing data as in the previous section. 
It uses training data from four cabins to predict the prices of two more cabins in the test data.
'''
import math
import numpy as np

x_train = np.array([[25, 2, 50, 1, 500], 
                  [39, 3, 10, 1, 1000],    
                  [82, 5, 20, 2, 120], 
                  [130, 6, 10, 2, 600]])
y_train = [127900, 222100,  268000, 460700]

x_test = np.array([[115, 6, 10, 1, 560], [13, 2, 13, 1, 1000]])


def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)

n_train = len(x_train) # number of data points in the training set

for test_item in x_test:
    d = np.empty(n_train) # d will hold the distances between this test data point and all the training data points
    for i, train_item in enumerate(x_train):
        d[i] = dist(test_item, train_item)
    nearest_index = np.argmin(d) # the nearest neighbour will be in y_train[nearest]
    print(y_train[nearest_index])