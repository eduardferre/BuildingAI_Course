# Intermediate level
'''
Suppose we have two coins. One is a normal 2 euro coin that comes heads up with 50% probability, and tails up also with 50% probability. 
The other coin, bought from the magicians' store, has heads on both sides. Good for party tricks and such. It comes heads up with 100% probability.

Suppose now that we choose one of the two coins at random so that either one can be picked with equal probability. The odds that we have the normal coin is thus 1:1.

Let's say the chosen coin keeps landing heads up. How confident can we be that it's the magic coin?

Let's use the naive Bayes method to calculate the odds for the magic coin. We may start with the odds 1:1 since each coin is equally 
probable to begin with. Each time we flip the coin and it lands heads up, the odds are multiplied by the likelihood ratio which is

r = P(heads | magic) / P(heads | normal) = 1 / 0.5 = 2
Your task: Starting from the odds 1:1 (which is represented as simply the numerical value 1.0), use the naive Bayes method to update 
the odds for the magic coin after n heads in a row. For example, after three heads (n=3), the odds should be 1 x 2 x 2 x 2 = 8.0.
'''
def flip(n):
    odds = 1.0         # start with 50% chance of the magic coin, which is the same as odds = 1:1
    r = 2
    for i in range(n):
        odds = odds * r           # edit here to update the odds
    print(odds)

n = 3
flip(n)
print('#################################')

# Advanced level
'''
We have two dice in our desk drawer. One is a normal, plain die with six sides such that each of the sides comes up with equal 1/6 probability. 
The other one is a loaded die that also has six sides, but that however gives the outcome 6 with every second try on the average, the other five sides being equally probable.

Thus with the first, normal die the probabilities of each side are the same, 0.167 (or 16.7 %). With the second, loaded die, the probability of 
6 is 0.5 (or 50 %) and each of the other five sides has probability 0.1 (or 10 %).

The following program gets as its input the choice of the die and then simulates a sequence of ten rolls.

Your task: starting from the odds 1:1, use the naive Bayes method to update the odds after each outcome to decide which of the dice is more likely.
Edit the function bayes so that it returns True if the most likely die is the loaded one, and False otherwise. Remember to be careful with the indices when accessing list elements!
'''
import numpy as np

p1 = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]   # normal
p2 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]   # loaded

def roll(loaded):
    if loaded:
        print("rolling a loaded die")
        p = p2
    else:
        print("rolling a normal die")
        p = p1

    # roll the dice 10 times
    # add 1 to get dice rolls from 1 to 6 instead of 0 to 5
    sequence = np.random.choice(6, size=10, p=p) + 1 
    for roll in sequence:
        print("rolled %d" % roll)
        
    return sequence

def bayes(sequence):
    odds = 1.0           # start with odds 1:1
    r12345 = 0.1 / (1/6)
    r6 = 0.5 / (1/6)
    for roll in sequence:
        # edit here to update the odds
        if roll == 6:
            odds *= r6
        else:
            odds *= r12345
    if odds > 1:
        return True
    else:
        return False

sequence = roll(True)
if bayes(sequence):
    print("I think loaded")
else:
    print("I think normal")