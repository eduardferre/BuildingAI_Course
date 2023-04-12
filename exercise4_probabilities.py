# Intermediate level
'''
Recall the program that prints out the word 'dog' with 20% probability. Modify the program so that it prints either the word 'dog' 
or the word 'cat' (but never both, because either you're a dog person or a cat person, but not both, right?)

Change the probability of the word 'dog' to be 80% probability (because apparently there are more dog lovers than cat lovers in the world) 
so that the probability of the word 'cat' is 20%.
'''
import random

def main():
    prob = 0.80
    if random.random() <= prob:
        print('dog')
    else:
        print('cat')

main()
print("###########")

# Advanced level
'''
Write a program that prints "I love" followed by one word: the additional word should be 'dogs' with 80% probability, 'cats' with 10% probability, and 'bats' with 10% probability.

Here's an example output:

I love bats
'''
import random

def main():
    
    rand = random.random()
    if rand <= 0.8:
        favourite = "dogs"  # change this
    elif rand > 0.8 and rand <= 0.9:
        favourite = "cats"  # change this
    else:
        favourite = "bats"  # change this
    print("I love " + favourite) 

main()