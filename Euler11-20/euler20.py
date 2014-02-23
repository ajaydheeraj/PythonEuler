#sum of digits in 100!
from math import factorial
print sum([int(x) for x in str(factorial(100))])

#if you want me to make my own function...

def factorial1(n):
    return n * factorial(n-1)
print sum(int(x) for x in str(factorial1(100)))
