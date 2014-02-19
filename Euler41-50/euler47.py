from collections import defaultdict
import primesieve
sv = primesieve.sieve(10000)

def factor(num):
    sivpos = 0
    factorization = defaultdict(int)
    while(num != 1):
        p = sv[sivpos]
        if num % p == 0:
            factorization[p] += 1
            num /= p
        else: 
            sivpos += 1
    return factorization

def u(num, l):
    return (len(factor(num)) == l)

z = 4
i = 2
ncons = 0

while ncons < z:
    if i % 100 == 0:
        print(i) #i can't stand a blank screen
    if u(i, z):
        ncons +=1
    else:
        ncons = 0
    i += 1
print(i - z)



