# Intermediate level
'''
Write a program that counts the number of occurrences of "11" in an input sequence of zeros and ones. 
The input of the program is just the sequence and it should return a single number, which is the number of occurrences of "11".
'''
def count11(seq):
   # define this function and return the number of occurrences as a number
   num = 0
   i = 0


   while i < len(seq):
       if i > 0 and seq[i] == 1 and seq[i-1] == 1:
           num += 1
       i += 1

   return num

print(count11([0, 0, 1, 1, 1, 0])) # this should print 2

# Advanced level
'''
Write a program that generates 10000 random zeros and ones where the probability of one is p1 and the probability of zero is 1-p1 
(hint: np.random.choice([0,1], p=[1-p1, p1], size=10000)), counts the number of occurrences of 5 consecutive ones ("11111") 
in the sequence, and outputs this number as a return value. Check that for p1 = 2/3, the count is close to 10000 x (2/3)^5 ≈ 1316.9.
'''
import numpy as np

def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    seq = np.random.choice([0, 1], p=[1-p1, p1], size=10000)
    print(seq)
    return seq

def count(seq):
    # insert code to return the number of occurrences of 11111 in the sequence
    
    i = 0
    count = 0

    while i < len(seq):
        if i > 3 and seq[i] == 1 and seq[i-1] == 1 and seq[i-2] == 1 and seq[i-3] == 1 and seq[i-4] == 1:
            count += 1
        i += 1
                
    return count 

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))