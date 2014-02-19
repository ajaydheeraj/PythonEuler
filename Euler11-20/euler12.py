#What is the value of the first triangle number to have over five hundred divisors?
from math import sqrt

def nterm(x):
    return 0.5 * x * (x+1)

def divisors(x):
    return set(reduce(list.__add__, ([i,x//i] for i in range(1,int(x**0.5) + 1) if not x % i)))
'''
an explanation of divisors function
def divisors(x):
    return set(reduce(list.__add__, ([i,x//i] for i in range(1,int(x**0.5) + 1) if not x % i)))
return set(
reduce(
adding to a list
a number, and the input divided by that number
that number is found for i in a range from 1 to the sqrt of the input if the input % the number == 0
the set weens out duplicates
and the reduce constantly adds to the list, making it bigger
found this on a stackoverflow forum, no credit taken!
'''


def euler12(z):
    x = 10001
    while len(divisors(nterm(x)))< z:
        x += 2
    return nterm(x)

print euler12(501)


