import math

fact = [math.factorial(i) for i in range(10)]

def getsum(i):
    return sum(fact[int(x)] for x in str(i))

print sum(i for i in xrange(1000000) if getsum(i) == i)
