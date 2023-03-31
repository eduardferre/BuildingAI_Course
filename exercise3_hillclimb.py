# Intermediate level
'''
Let the elevation at each point on the mountain be stored in array h of size 100. 
The elevation at the leftmost point is thus stored in h[0] and the elevation at the rightmost point is stored in h[99].

The following program starts at a random position and keeps going to the right until Venla can no longer go up. 
To make it easier to avoid falling off the map at the boundaries, we set both h[0] and h[100] equal to zero which is lower than any of the values in between.

You can see the result in the above chart where the starting point is marked with a small green box and the point where Venla 
stops is marked with a small red triangle. This works fine as long as the summit is to her right, but maybe it is to the left?

Edit the program so that Venla doesn't stop climbing if she can go up either by moving left or right. If both ways go up, either one is good. 
To check how your climbing algorithm works in action, you can plot the results of your hill climbing using the Plot button. The summit will be marked with a blue triangle.
'''
import math
import random             	# just for generating random mountains   
import numpy as np     
import matplotlib.pyplot as plt                      	 

# generate random mountains                                                                               	 
w = [random.random()/3, random.random()/3, random.random()/3]
h = [1.+math.sin(1+x/6.)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]
h[0] = 0.0; h[99] = 0.0

def climb(x, h):
    # keep climbing until we've found a summit
    summit = False

    # edit here
    while not summit:
        summit = True         # stop unless there's a way up
        if h[x + 1] > h[x] and h[x+1]:
            x = x + 1         # right is higher, go there
            summit = False    # and keep going
        
        if h[x - 1] > h[x]:
            x =  x - 1
            summit = False
        
    return x


def main(h):

    # start at a random place                                                                                  	 
    x0 = random.randint(1, 98)
    x = climb(x0, h)
    plt.plot(h)
    array = np.array(h)
    max_index = array.argmax()
    plt.plot(max_index, max(h), marker="X", markersize=10)
    plt.plot(x0, h[x0], marker="s", markersize=10)
    plt.plot(x, h[x], marker="^", markersize=10)
    plt.show()

    print("Venla started at %d and got to %d" % (x0, x))
    return x0, x

main(h)
print("############################")

# Advanced level
'''
The following program starts at a random position and keeps going to the right until Venla can no longer go up. 
However, perhaps the mountain is a bit rugged which means it's necessary to look a bit further ahead.

Edit the program so that Venla doesn't stop climbing as long as she can go up by moving up to five steps either left or right. 
If there are multiple choices within five steps that go up, any one of them is good. To check how your climbing algorithm works in action, 
you can plot the results of your hill climbing using the Plot button. As a reminder, the summit will be marked with a blue triangle.
'''                            	 

# generate random mountains                                                                               	 

w = [.05, random.random()/3, random.random()/3]
h = [1.+math.sin(1+x/.6)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]

def climb(x, h):
    # keep climbing until we've found a summit
    summit = False

    # edit here
    while not summit:
        summit = True         # stop unless there's a way up
        for x_new in range(max(0, x-5), min(99, x+5)):
            if h[x_new] > h[x]:
                x = x_new         # right is higher, go there
                summit = False    # and keep going
        
    return x


def main(h):
    # start at a random place                                                                                  	 
    x0 = random.randint(1, 98)
    x = climb(x0, h)
    plt.plot(h)
    array = np.array(h)
    max_index = array.argmax()
    plt.plot(max_index, max(h), marker="X", markersize=10)
    plt.plot(x0, h[x0], marker="s", markersize=10)
    plt.plot(x, h[x], marker="^", markersize=10)
    plt.show()

    return x0, x

main(h)
