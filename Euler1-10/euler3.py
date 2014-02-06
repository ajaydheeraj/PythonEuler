from primesieve import *
# The above code is excessively documented

p = sieve(int(600851475143**0.5)) #sieve up to the square root of number
l = [] #empty list
for i in p:
    if 600851475143 % i == 0: # if a number in the sieve and the giant number divide evenly
        l.append(i)
print l[-1] #print the final element in the list
