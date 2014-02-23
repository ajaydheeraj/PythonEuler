from primesieve import *
# The above code is excessively documented
n = 600851475143
p = sieve(int(n**0.5)) #sieve up to the square root of number
for i in p[::-1]:
    if not n % i: # if a number in the sieve(the largest) and the giant number divide evenly
        print i #print the number
        break   #we're done here
