# Advanced level
'''
You are given a set of three input values and you also have multiple alternative sets of three coefficients. 
Calculate the predicted output value using the linear formula combined with the logistic activation function.

Do this with all the alternative sets of coefficients. Which of the coefficient sets yields the highest sigmoid output?
'''
import math
import numpy as np

x = np.array([4, 3, 0])
c1 = np.array([-.5, .1, .08])
c2 = np.array([-.2, .2, .31])
c3 = np.array([.5, -.1, 2.53])

def sigmoid(z):
    # add your implementation of the sigmoid function here
    out = 1 / (1 + math.exp(-z))
    print(out)
    return out

out1 = sigmoid(x @ c1)
out2 = sigmoid(x @ c2)
out3 = sigmoid(x @ c3)

# calculate the output of the sigmoid for x with all three coefficients