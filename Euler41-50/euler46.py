from primesieve import *
p = sieve(10000) #list of many primes up to arbitrary point
s = [x**2 for x in range(1001) if x **2 < 100000] #ditto
n = range(3,100000,2) #must be ordered, have to find FIRST
l = set(i + 2 * a for i in p for a in s) #not necessary
for i in n : 
    if i not in l: #if a number in the range isn't in the special list
        print i
        break
