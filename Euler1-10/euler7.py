def isprime(n):
    for i in xrange(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

l = []
x = 2
while len(l) < 10001:
    if isprime(x):
        l.append(x)
    x += 1
print l[-1]
 #OR
from primesieve import *
print sieve(1000000)[10000]
#the 1000000 was just an arbitrarily long number
