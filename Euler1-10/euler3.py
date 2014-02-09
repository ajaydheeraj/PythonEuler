from primesieve import *
# The above code is excessively documented

p = sieve(int(600851475143**0.5)) #sieve up to the square root of number
l = [] #empty list
n = 600851475143
for i in p[::-1]:
    if n % i == 0: # if a number in the sieve(the largest) and the giant number divide evenly
        print i #print the number
        break   #we're done here
