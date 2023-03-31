# Intermediate level
'''
The program below prints the total emissions on the route PAN, AMS, CAS, NY, HEL (in port indices route 0, 1, 2, 3, 4) 
in kilograms, which is 504.5 kg. Modify the program so that it prints out the carbon emissions of all the possible routes. 
The solution for the previous exercise should be useful here.
'''
def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
    ports = [0, 1, 2, 3, 4]

    # https://sea-distances.org/
    # nautical miles converted to km

    D = [
            [0,8943,8019,3652,10545],
            [8943,0,2619,6317,2078],
            [8019,2619,0,5836,4939],
            [3652,6317,5836,0,7825],
            [10545,2078,4939,7825,0]
        ]

    # https://timeforchange.org/co2-emissions-shipping-goods
    # assume 20g per km per metric ton (of pineapples)


    co2 = 0.020

    for port1 in ports:
        for port2 in ports:
            for port3 in ports:
                for port4 in ports:
                        route = [0, port1, port2, port3, port4]
                        if set(route) == set(range(5)):
                            distance = D[route[0]][route[1]] + D[route[1]][route[2]] + D[route[2]][route[3]] + D[route[3]][route[4]]
                            emissions = distance * co2
                            print(' '.join([portnames[i] for i in route]) + " %.1f kg" % emissions)
    
main()
print("############################")

# Advanced level
'''
Building on the previous solution, modify the code so that it finds the route with minimum carbon emissions and prints it out. 
Again, the program should work for any number of ports. You can assume that the distances between the ports are given in an array 
of the appropriate size so that the distance between ports i and j is found in D[i][j].
'''
portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# https://sea-distances.org/
# nautical miles converted to km

D = [
        [0,8943,8019,3652,10545],
        [8943,0,2619,6317,2078],
        [8019,2619,0,5836,4939],
        [3652,6317,5836,0,7825],
        [10545,2078,4939,7825,0]
    ]

# https://timeforchange.org/co2-emissions-shipping-goods
# assume 20g per km per metric ton (of pineapples)

co2 = 0.020

# DATA BLOCK ENDS

# these variables are initialised to nonsensical values
# your program should determine the correct values for them
smallest = 1000000
bestroute = [0, 0, 0, 0, 0]

def permutations(route, ports):
    # write the recursive function here
    # remember to calculate the emissions of the route as the recursion ends
    # and keep track of the route with the lowest emissions
    low = smallest
    for port1 in ports:
        for port2 in ports:
            for port3 in ports:
                for port4 in ports:
                        route = [0, port1, port2, port3, port4]
                        if set(route) == set(range(5)):
                            distance = D[route[0]][route[1]] + D[route[1]][route[2]] + D[route[2]][route[3]] + D[route[3]][route[4]]
                            emissions = distance * co2
                            if emissions < low:
                                low = emissions
                                bestroute = [0, port1, port2, port3, port4]
    
    return [bestroute, low]
    

def main():
    # Do not edit any (global) variables using this function, as it will mess up the testing

    # this will start the recursion 
    [bestroute, smallest] = permutations([0], list(range(1, len(portnames))))

    # print the best route and its emissions
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)

main()