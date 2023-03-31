# Intermediate level
'''
In this exercise you need to list all the possible routes that start from Panama and visit each of the other ports exactly once.

Have a look at the program further down the page. Go ahead and run it. You'll see that the first thing it prints is PAN AMS AMS AMS AMS. 
Nice for the sailors but bad for pineapple lovers anywhere else but Amsterdam.

Each port is denoted by a number instead of a string: PAN is 0, AMS is 1 and so on. It is often easier to work with integer numbers instead of strings when programming. 
Keep this mapping in mind when we interpret the results of the program.

Fix the program by adding an if statement that checks that the route includes all of the ports. 
In other words, check that each of the numbers 0, 1, 2, 3, 4 are included in the list route.

Do not change the print statement given in the template (although you can add more print statements for debugging purposes).
'''
def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    port1 = 0
    for port2 in range(1, 5):
        for port3 in range(1, 5):
            for port4 in range(1, 5):
                for port5 in range(1, 5):
                    route = [port1, port2, port3, port4, port5]

                    # Modify this if statement to check if the route is valid
                    if set(route) == set(range(5)): 
                        # you can check that the route includes all ports (numbered 0, 1, ..., 4) 
                        # easily by using Python sets.
                        # do not modify this print statement
                        print(' '.join([portnames[i] for i in route]))

main()
print("###################")

# Advanced level
'''
In this exercise you need to list all the possible routes that start from Panama and visit each of the other ports exactly once.

The template code below contains an incomplete permutations function which takes as input a specified route and a list of port names absent from that route. 
Modify the function so that it prints out all the possible orderings of the ports that always begin with Panama (PAN).

The mathematical term for such orderings is a permutation. Note that your program should work for an input portnames list of any length. 
The order in which the permutations are printed doesn't matter.

As the output the function should print each permutation on its own row, as one string, with the port names separated by spaces. 
For this, you can use the join function as follows: print(' '.join([portnames[i] for i in route])).
'''
portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

def permutations(route, ports):
    # Write your recursive code here
    for port1 in ports:
        for port2 in ports:
            for port3 in ports:
                for port4 in ports:
                    route = [0, port1, port2, port3, port4]
                    if set(route) == set(range(5)):
                        # Print the port names in route when the recursion terminates
                        print(' '.join([portnames[i] for i in route]))


# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames))))
print("###################")

def permutations(route, ports):
    if len(ports) < 1:
        print(' '.join([portnames[i] for i in route]))
    else:
        for i in range(len(ports)):
            permutations(route+[ports[i]], ports[:i]+ports[i+1:])
 
permutations([0], list(range(1, len(portnames))))