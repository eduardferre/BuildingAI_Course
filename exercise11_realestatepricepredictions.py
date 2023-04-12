# Intermediate level
'''
Edit the code so that it prints out the prices of multiple cabins in one go.
'''
# input values for three mökkis: 
#  - size [m^2], 
#  - size of the sauna [m^2], 
#  - distance to water [m], 
#  - number of indoor bathrooms, 
#  - proximity of neighbors [m]
X = [[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]]

# coefficient values
c = [3000, 200 , -50, 5000, 100]

def predict(X, c):
    # write a loop that goes over the cabin data and for each cabin prints out 
    # the predicted price of the cabin you can assume that the number of inputs
    # and the number of coefficients are the same
    i = 0
    for x in X:
        price = c[0]*x[0] + c[1]*x[1] + c[2]*x[2] + c[3]*x[3] + c[4]*x[4]          
        print(price)

predict(X, c)
print('#################################')

# Advanced level
'''
Edit the following program so that it can process multiple cabins that may be described by any number of details (like five below), at the same time.
You can assume that each of the lists contained in the list x and the coefficients c contain the same number of elements.
'''
# input values for three mökkis: size, size of sauna, distance to water, number of indoor bathrooms, 
# proximity of neighbors
X = [[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]]
c = [3000, 200, -50, 5000, 100]    # coefficient values

def predict(X, c):
    i = 0
    for x in X:
        price = 0
        for y, z in zip(x, c):
            price += y*z          
        print(price)

predict(X, c)


'''
The cumbersome sum c[0]*x[0] + c[1]*x[1] + c[2]*x[2] + c[3]*x[3] + c[4]*x[4] can be easily replaced by a for loop. However, 
there are even more elegant ways to do this using the numerical computation package numpy.
'''
import numpy as np

x = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100]])
c = np.array([3000, 200 , -50, 5000, 100])

print(x @ c)