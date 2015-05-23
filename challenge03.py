#!/usr/bin/python

import sys
from time import sleep


PRIMES = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(PRIMES)


filename = sys.argv[1]
lines = open(filename, 'r').readlines()
lines.pop(0)


numbers = open('numbers.txt', 'r')

prime_count = {prime:0 for prime in PRIMES}

for number in numbers.readlines():

    number = float(number)
    #print(number)
    
    #print("")

    #number = 394019227828.0
    
    for _ in range(8):
        number = number / 5463763535.456456456456
        #print('NUM: %f' % number)
        #print('{:.2%}'.format(number))
        
        print( "%.5f" % number)
    
    #if number % 1 == 0.0:
        #print("Whole Number")
    
    
    #number = number / 11
    #number = number / 7
    #number = number / 37
    #number = number / 2
    #number = number / 2
    #number = number / 2
    #number = number / 31
    #number = number / 3
    #number = number / 3
    #number = number / 3
    #number = number / 3
    #number = number / 31
    #number = number / 3
    #number = number / 2

    #for prime in PRIMES:
        #print(prime, number % prime)

    #print(number)
    
    exit()
    
    while True:
        if number == 1:
            break;

        for prime in reversed(PRIMES):
            print("TRY PRIME", prime)
            if number % prime == 0:
                print('Prime', prime)
                sleep(0.2)
                prime_count[prime] = prime_count[prime] + 1
                number = number / prime
                print('Number', number)
                break
                
                
print(prime_count)


