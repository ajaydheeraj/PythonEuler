from math import log10 ,floor
import primesieve
def rotate(n):
    p = floor(log10(n))
    last = int(n % (10 ** p))
    first = (n - last ) / 10 ** p
    return int(last * 10 + first)

def rotatelist(n):
    l = []
    lenn = floor(log10(n)) + 1
    i = 0
    while i < lenn:
        l.append(n)
        n = rotate(n)
        i+=1
    return l
def toss(n):
    nums = [int(i) for i in str(n)]
    bad = [0, 2, 4, 6, 8, 5]
    for b in bad:
        if b in nums:
            return True
    return False

def prune(plist):
    newlist = []
    for i,n in enumerate(plist):
        if not toss(n):
            newlist.append(n)
    newlist.insert(0,2)
    newlist.insert(2,5)
    return newlist

count = 0
primes = set(primesieve.sieve(1000000))
pruned = prune(primes)

# cs = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]
for x in pruned:
    cycs = rotatelist(x)
    if sum(perm in pruned for perm in cycs) == len(cycs):
        count += 1
print(count)
