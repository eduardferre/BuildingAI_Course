# Intermediate level
'''
We have trained a simple neural network with a larger set of cabin price data. The network predicts the price of the cabin based on the attributes of 
the cabin. The network consists of an input layer with five nodes, a hidden layer with two nodes, a second hidden layer with two nodes, and finally an 
output layer with a single node. In addition, there is a single bias node for each hidden layer and the output layer.

The program below uses the weights of this trained network to perform what is called a forward pass of the neural network. The forward pass is running 
the input variables through the neural network to obtain output, in this case the price of a cabin of given attributes.

The program is incomplete though. The bias nodes are not used in the version below, and the activation functions for the hidden layers and the output 
layer have not been properly defined.

Modify the program to use the bias nodes, and to use the ReLU activation function for the hidden nodes, and a linear (identity) activation for the 
output node. ReLU activation function returns either the input value of the function, or zero, whichever is the largest, and linear activation just 
returns the input as output. After these are done, get a prediction for the price of a cabin which is described by the following feature vector [74, 5, 10, 2, 100].
'''
import numpy as np

w0 = np.array([[ 1.19627687e+01,  2.60163283e-01],
               [ 4.48832507e-01,  4.00666119e-01],
                              [-2.75768443e-01,  3.43724167e-01],
                   [ 2.29138536e+01,  3.91783025e-01],
                   [-1.22397711e-02, -1.03029800e+00]])

w1 = np.array([[11.5631751 , 11.87043684],
                   [-0.85735419,  0.27114237]])

w2 = np.array([[11.04122165],
                   [10.44637262]])

b0 = np.array([-4.21310294, -0.52664488])
b1 = np.array([-4.84067881, -4.53335139])
b2 = np.array([-7.52942418])

x = np.array([[111, 13, 12, 1, 161],
                 [125, 13, 66, 1, 468],
                 [46, 6, 127, 2, 961],
                 [80, 9, 80, 2, 816],
                 [33, 10, 18, 2, 297],
                 [85, 9, 111, 3, 601],
                 [24, 10, 105, 2, 1072],
                 [31, 4, 66, 1, 417],
                 [56, 3, 60, 1, 36],
                 [49, 3, 147, 2, 179]])
y = np.array([335800., 379100., 118950., 247200., 107950., 266550.,  75850.,
                93300., 170650., 149000.])


def hidden_activation(z):
    # ReLU activation. fix this!
    for i, item in enumerate(z):
        if item < 0:
            z[i] = 0
    return z

def output_activation(z):
    # identity (linear) activation. fix this!
        return z

x_test = [[72, 2, 25, 3, 450], [60, 3, 15, 1, 300], [74, 5, 10, 2, 100]]
for item in x_test:
    h1_in = np.dot(item, w0) + b0 # this calculates the linear combination of inputs and weights. it is missing the bias term, fix it!
    h1_out = hidden_activation(h1_in) # apply activation function
    
    h2_in = np.dot(h1_out, w1) + b1 # the output of the previous layer is the input for this layer. it is missing the bias term, fix it!
    h2_out = hidden_activation(h2_in)
    
    out_in = np.dot(h2_out, w2) + b2
    out = output_activation(out_in)
    print(out)
print('#################################')

# Advanced level
'''
After these are done, get a prediction for the price of a cabin which is described by the following feature vector [82, 2, 65, 3, 516].
'''
import numpy as np

w0 = np.array([[ 1.19627687e+01,  2.60163283e-01],
               [ 4.48832507e-01,  4.00666119e-01],
                   [-2.75768443e-01,  3.43724167e-01],
                   [ 2.29138536e+01,  3.91783025e-01],
                   [-1.22397711e-02, -1.03029800e+00]])

w1 = np.array([[11.5631751 , 11.87043684],
                   [-0.85735419,  0.27114237]])

w2 = np.array([[11.04122165],
                   [10.44637262]])

b0 = np.array([-4.21310294, -0.52664488])
b1 = np.array([-4.84067881, -4.53335139])
b2 = np.array([-7.52942418])

x = np.array([[111, 13, 12, 1, 161],
                 [125, 13, 66, 1, 468],
                 [46, 6, 127, 2, 961],
                 [80, 9, 80, 2, 816],
                 [33, 10, 18, 2, 297],
                 [85, 9, 111, 3, 601],
                 [24, 10, 105, 2, 1072],
                 [31, 4, 66, 1, 417],
                 [56, 3, 60, 1, 36],
                 [49, 3, 147, 2, 179]])
y = np.array([335800., 379100., 118950., 247200., 107950., 266550.,  75850.,
                93300., 170650., 149000.])


def hidden_activation(z):
    # ReLU activation. fix this!
    for i, item in enumerate(z):
        if item < 0:
            z[i] = 0
    return z

def output_activation(z):
    # identity (linear) activation. fix this!
        return z

x_test = [[82, 2, 65, 3, 516]]
for item in x_test:
    h1_in = np.dot(item, w0) + b0 # this calculates the linear combination of inputs and weights
    h1_out = hidden_activation(h1_in) # apply activation function

    h2_in = np.dot(h1_out, w1) + b1
    h2_out = hidden_activation(h2_in)

    out_in = np.dot(h2_out, w2) + b2
    out = output_activation(out_in)
    
    # fill out the missing parts:
    # the output of the first hidden layer, h1_out, will need to go through
    # the second hidden layer with weights w1 and bias b1
    # and finally to the output layer with weights w2 and bias b2.
    # remember correct activations: relu in the hidden layers and linear (identity) in the output
    
    print(out)