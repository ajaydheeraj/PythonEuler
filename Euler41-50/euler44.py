# def pent(x):
#     return (x * (3*x - 1)) / 2
# pent1 = set(pent(i) for i in range(1,10000))
# personally i like the way below better
pent = set( (i * (3 * i - 1)) / 2 for i in range(1,10000))
for i in pent :
    for j in pent :
        if i + j in pent  and i - j in pent :
            print abs(j - i)
            break
