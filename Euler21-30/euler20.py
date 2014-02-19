#sum of digits in 100!
from math import factorial
print sum([int(x) for x in str(factorial(100))])
