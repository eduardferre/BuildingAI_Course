# Intermediate level
'''
1D simulated annealing: modify the program below to use simulated annealing instead of plain hill climbing. 
In simulated annealing the probability of accepting a solution that lowers the score is given by prob = exp(-(S_old - S_new)/T). 
Setting the temperature T and gradually decreasing can be done in many ways, some of which lead to better outcomes than others. 
A good choice in this case is for example: T = 2*max(0, ((steps-step*1.2)/steps))**3.

Your task is to modify the code to use simulated annealing. Use the cooling schedule for setting the temperature provided above, 
and modify the acceptance criterion from only accepting upward moves to accepting also downward moves with the proper probability. 
Remember that in this exercise the score in simulated annealing is the height of a given location on the mountain. 
Also note that you will need to handle T=0 case separately, since the acceptance probability for a worse score should be zero for zero temperature, 
but the formula used for the probability will result in division by zero.

If plotting the code takes too long, use this gist to plot the code locally on your computer. It should be significantly faster.
'''
import math, random        	# just for generating random mountains                                 	 
import numpy as np
import matplotlib.pyplot as plt

n = 10000 # size of the problem: number of possible solutions x = 0, ..., n-1

# generate random mountains                                                                               	 
def mountains(n):
    h = [0]*n
    for i in range(50):
        c = random.randint(20, n-20)
        w = random.randint(3, int(math.sqrt(n/5)))**2
        s = random.random()
        h[max(0, c-w):min(n, c+w)] = [h[i] + s*(w-abs(c-i)) for i in range(max(0, c-w), min(n, c+w))]

    # scale the height so that the lowest point is 0.0 and the highest peak is 1.0
    low = min(h)
    high = max(h)
    h = [y - low for y in h]
    h = [y / (high-low) for y in h]
    return h

h = mountains(n)

# start at a random place
x0 = random.randint(1, n-1)
x = x0

# keep climbing for 5000 steps
steps = 5000

def main(h, x):
    n = len(h)
    # the climbing starts here
    for step in range(steps):
        # this is our temperature to to be used for simulated annealing
        # it starts large and decreases with each step. you don't have to change this
        T = 2*max(0, ((steps-step*1.2)/steps))**3

        # let's try randomly moving (max. 1000 steps) left or right
        # making sure we don't fall off the edge of the world at 0 or n-1
        # the height at this point will be our candidate score, S_new
        # while the height at our current location will be S_old
        x_new = random.randint(max(0, x-1000), min(n-1, x+1000))

        if h[x_new] > h[x]:
            x = x_new           # the new position is higher, go there
        else:
            if T > 0:
                prob = np.exp(-(h[x] - h[x_new])/T)
            else:              
                prob = 0.0  

            if random.random() < prob:
                x = x_new
            else:
                pass     
                
                # add simulated annealing here. remember to handle T=0
                # correctly!

    return x

x = main(h, x0)
print("ended up at %d, highest point is %d" % (x, np.argmax(h)))
print("#################################")
plt.plot(h)
array = np.array(h)
max_index = array.argmax()
plt.plot(max_index, max(h), marker="X", markersize=10)
plt.plot(x0, h[x0], marker="s", markersize=10)
plt.plot(x, h[x], marker="^", markersize=10)
plt.show()

# Advanced level
'''
Let's use simulated annealing to solve a simple two-dimensional optimization problem. 
The following code runs 50 optimization tracks in parallel (at the same time). It currently only looks around the current solution 
and only accepts moves that go up. Modify the program so that it uses simulated annealing.

Remember that the probability of accepting a solution that lowers the score is given by prob = exp(-(S_old - S_new)/T). 
Remember to also adjust the temperature in a way that it decreases as the simulation goes on, and to handle T=0 case correctly.

Your goal is to ensure that on the average, at least 30 of the optimization tracks find the global optimum (the highest peak).

If plotting the code takes too long, use this gist to plot the code locally on your computer. It should be significantly faster.
'''
import numpy as np
import random

N = 100     # size of the problem is N x N                                      
steps = 3000    # total number of iterations                                        
tracks = 50

# generate a landscape with multiple local optima                                          
def generator(x, y, x0=0.0, y0=0.0):
    return np.sin((x/N-x0)*np.pi)+np.sin((y/N-y0)*np.pi)+\
        .07*np.cos(12*(x/N-x0)*np.pi)+.07*np.cos(12*(y/N-y0)*np.pi)

x0 = np.random.random() - 0.5
y0 = np.random.random() - 0.5
h = np.fromfunction(np.vectorize(generator), (N, N), x0=x0, y0=y0, dtype=int)
peak_x, peak_y = np.unravel_index(np.argmax(h), h.shape)

# starting points                                                               
x = np.random.randint(0, N, tracks)
y = np.random.randint(0, N, tracks)

def main():
    global x
    global y

    for step in range(steps):
        # add a temperature schedule here
        T = 1
        # update solutions on each search track                                     
        for i in range(tracks):
            # try a new solution near the current one                               
            x_new = np.random.randint(max(0, x[i]-2), min(N, x[i]+2+1))
            y_new = np.random.randint(max(0, y[i]-2), min(N, y[i]+2+1))
            S_old = h[x[i], y[i]]
            S_new = h[x_new, y_new]

            # change this to use simulated annealing
            if S_new > S_old:
                x[i], y[i] = x_new, y_new   # new solution is better, go there       
            else:
                pass                        # if the new solution is worse, do nothing

    # Number of tracks found the peak
    print(sum([x[j] == peak_x and y[j] == peak_y for j in range(tracks)])) 
main()
