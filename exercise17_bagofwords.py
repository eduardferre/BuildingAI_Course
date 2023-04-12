# Intermediate level
'''
Your task is to write a function that calculates the distances (or differences) between a pair of lines in the This Little Piggy rhyme.

Every row in the list data represents one line in the rhyme.

When you run the code, you see that the output of the whole program is a list of lists. 
When your function works correctly, each list will contain the distances between a single row and all the other rows in data.

Note that the program will compare every row also with itself. In this case – when the compared rows are the same – their distance will be zero.

You can use the function abs(x-y) to calculate the distance between numbers x and y, where x comes from list row1 and y comes from row2.

Your program must work with any text, not only with the rhyme This Little Piggy.
'''
# this data here is the bag of words representation of This Little Piggy
data =  [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def distance(row1, row2):
    # fix this function so that it returns 
    # the sum of differences between the occurrences
    # of each word in row1 and row2.
    # you can assume that row1 and row2 are lists with equal length, containing numeric values.
    sum_dif = 0
    for r1, r2 in zip(row1, row2):
        sum_dif += abs(r1-r2)
    return sum_dif

def all_pairs(data):
    # this calls the distance function for all the two-row combinations in the data
    # you do not need to change this
    dist = [[distance(sent1, sent2) for sent1 in data] for sent2 in data]
    print(dist)

all_pairs(data)
print('#################################')

# Advanced level
'''
Your task is to write a program that calculates the distances (or differences) between every pair of lines
in the This Little Piggy rhyme and finds the most similar pair. Use the Manhattan distance (also called Taxicab distance) as your distance metric.

You can start by building a numpy array to store all the distances. Notice that the diagonal elements in the 
array (elements at positions [i, j] with i=j) will be equal to zero. This happens because the program will compare 
every row also with itself. To avoid selecting those elements, you can assign the value np.inf (the maximum possible floating point value). 
To do this, it's necessary to make sure the type of the array is float. Do not use np.float to set the type of the array, as it is deprecated. 
Use Python's built-in type float instead.

A quick way to get the index of the element with the lowest value in a 2D array (or in fact, any dimension) is by the function

np.unravel_index(np.argmin(dist), dist.shape))

where dist is the 2D array. This will return the index as a list of length two. If you're curious, here's an intuitive 
explanation of the function, and here's its documentation.
'''
import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=np.cfloat)
    for m, item_m in enumerate(data):
        for n, item_n in enumerate(data):
            diff = 0
            for c, item_c in enumerate(data[m]):
                diff += abs(data[m][c]-data[n][c])
            dist[m][n] = diff

    for i, item_i in enumerate(dist):
        for j, item_j in enumerate(dist[i]):
            if i == j:
                dist[i][j] = np.Inf
    
    print(np.unravel_index(np.argmin(dist), dist.shape))

find_nearest_pair(data)

