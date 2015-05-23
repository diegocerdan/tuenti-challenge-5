#!/usr/bin/python

import sys

filename = sys.argv[1]
lines = open(filename, 'r').readlines()
lines.pop(0)

def rwh_primes1(start, end):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (end/2)
    for i in xrange(3,int(end**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((end-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,end/2) if sieve[i]]



primes = rwh_primes1(1, pow(10, 8))

semiprime = [False] * (pow(10, 8) + 1)
for prime_a in primes:
    for prime_b in primes:
        multiplication = prime_a * prime_b
        if multiplication > pow(10, 8):
            break
        semiprime[prime_a * prime_b] = True 

for line in lines:
    start, end = line.split()
    start = int(start)
    end = int(end)

    number_of_semiprimes = 0
    for number in xrange(start, end + 1):
        if semiprime[number]:
            number_of_semiprimes = number_of_semiprimes + 1
            
    print(number_of_semiprimes)

