from primesieve import *
p = sieve(10000)
s = [x**2 for x in range(1001) if x **2 < 100000]
n = (i for i in range(3,100000,2))
# for i in p:
#     for a in s:
#         l.append(i+2*a)
l = set(i + 2 * a for i in p for a in s)
for i in n :
    if i not in l:
        print i
        break
