# Intermediate level
'''
Write a program that uses statistics about the population and fishing industry employment to print out conditional probabilities of 
each nationality given that the winner works in the fishing industry.

The data is given in lists containing the population and the number of fishers in each country.

Output Example
Denmark 14.32%
...
Sweden 08.45%

'''
def main():
    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    populations = [5615000, 5439000, 324000, 5080000, 9609000]
    fishers = [1891, 2652, 3800, 11611, 1757]

    total_fishers = sum(fishers)
    total_population = sum(populations)

    i = 0
    probabilities = [0] * 5
    while i < len(countries):
        # write your solution here
        probabilities[i] = fishers[i] / total_fishers * 100
        i += 1

    for country, prob in zip(countries, probabilities):
        print("%s %.2f%%" % (country, prob)) # modify this to print correct results

main()
print("#################################")

# Advanced level
'''
Write a function that uses the above numbers and tries to guess the nationality of the winner when we know that the winner is a 
fisher and their gender (either female or male).

The argument of the function should be the gender of the winner ('female' or 'male'). The return value of the function should be a 
pair (country, probability) where country is the most likely nationality of the winner and probability is the probability of the country being the nationality of the winner.

Output Example
if the winner is male, my guess is he's from Finland; probability 08.56%
if the winner is female, my guess is she's from Norway; probability 23.98%
'''
countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
populations = [5615000, 5439000, 324000, 5080000, 9609000]
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69, 77, 400, 320, 26] 

def guess(winner_gender):
    if winner_gender == 'female':
        fishers = female_fishers
    else:
        fishers = male_fishers

    # write your solution here
    i = 0
    num = 0
    guess = None
    while i < len(countries):
        if fishers[i] > num:
            num = fishers[i]
            guess = countries[i]
            biggest = fishers[i] / sum(fishers) * 100
        i += 1
    
    return (guess, biggest)  

def main1():
    country, fraction = guess("male")
    print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (country, fraction))
    country, fraction = guess("female")
    print("if the winner is female, my guess is she's from %s; probability %.2f%%" % (country, fraction))

main1()