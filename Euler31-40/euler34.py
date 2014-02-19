import math

def getdigits(i):
    return [int(x) for x in str(i)]

print sum(i for i in xrange(3,1000000) if sum(map(math.factorial,getdigits(i))) == i)

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# count = 0
# for i in range(3,9999999):
#     if sum(map(factorial,getdigits(i))) == i:
#         count +=i
#         print count
