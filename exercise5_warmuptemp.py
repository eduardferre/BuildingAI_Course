# Advanced level
'''
Suppose the current solution has score S_old = 150 and you try a small modification to create a new solution with score S_new = 140. 
In the greedy solution, this new solution wouldn't be accepted because it would mean a decrease in the score. 
In simulated annealing, the new solution is accepted with a certain probability as explained above.

Modify the accept_prob function so that it returns the probability of accepting the new state using simulated annealing. 
The program should take the two score values (the current and the new) and the temperature value as arguments.
'''
import random
import numpy as np

def accept_prob(S_old, S_new, T):
    # this is the acceptance "probability" in the greedy hill-climbing method
    # where new solutions are accepted if and only if they are better
    # than the old one.
    # change it to be the acceptance probability in simulated annealing

    if S_new > S_old:
        return 1.0
    else:
        return np.exp(-(S_old - S_new)/T)


# the above function will be used as follows. this is shown just for
# your information; you don't have to change anything here
def accept(S_old, S_new, T):
    if random.random() < accept_prob(S_old, S_new, T):
        print(True)
    else:
        print(False)

def main():
    S_old = 150
    S_new = 140
    accept(S_old, S_new, 15)

main()