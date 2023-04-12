# Intermediate level
'''
Modify the program so it implements the calculation of the squared error. In other words, you should calculate 
the predicted prices for all the cabins in the data, subtract the predicted price from the actual price (which is given in the data), square the difference, and add them all up.

The program needs to work for any number of cabins and cabin features.
'''
import numpy as np

X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])
c = np.array([3000, 200 , -50, 5000, 100])    # coefficient values
 
def squared_error(X, y, c):
    sse = 0.0
    for xi, yi in zip(X, y):
        # add your code here: calculate the predicted price,
        # subtract it from the actual price yi, 
        # square the difference using (yi - prediction)**2, 
        # and add up all the differences in variable sse
        pred = np.dot(xi, c)
        sub = (yi - pred)**2
        sse += sub

    print(sse)

squared_error(X, y, c)
print('#################################')

# Advanced level
'''
Write a program that calculates the squared error for multiple sets of coefficient values and prints out the index of 
the set that yields the smallest squared error: this is a poor man's version of the least squares method where we only 
consider a fixed set of alternative coefficient vectors instead of finding the global optimum.
'''
import numpy as np

# data
X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array([[3000, 200 , -50, 5000, 100], 
              [2000, -250, -100, 150, 250], 
              [3000, -100, -150, 0, 150]])   

def find_best(X, y, c):
    smallest_error = np.Inf
    best_index = -1
    for index, coeff in enumerate(c):
        # edit here: calculate the sum of squared error with coefficient set coeff and
        # keep track of the one yielding the smallest squared error
        error = 0
        for x, yi in zip(X, y):
            error += (yi - np.dot(x, coeff))**2
        
        if error < smallest_error:
            smallest_error = error
            best_index = index
        
        
    print("the best set is set %d" % best_index)


find_best(X, y, c)

'''
To obtain the coefficient estimates, we call function lstsq (for least squares) in module linalg of the numpy package.
'''
import numpy as np

x = np.array([
             [25, 2, 50, 1, 500], 
             [39, 3, 10, 1, 1000], 
             [13, 2, 13, 1, 1000], 
             [82, 5, 20, 2, 120], 
             [130, 6, 10, 2, 600]
            ])   
y = np.array([127900, 222100, 143750, 268000, 460700])

c = np.linalg.lstsq(x, y)[0]
print(c)
print(x @ c)