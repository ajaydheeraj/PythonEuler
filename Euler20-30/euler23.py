from itertools import permutations
def sdivisors(x):
    y = set(reduce(list.__add__, ([i,x//i] for i in range(1,int(x**0.5) + 1) if not x % i)))
    y.remove(x)
    return sum(y)
def aod(n):
    if sdivisors(n) > n:
        return 'Abundant'
    elif sdivisors(n) == n:
        return 'Perfect'
    else:
        return 'Deficient'
l = []
for i in range(1,28124):
    if aod(i) == 'Abundant':
      l.append(i)
print l[:100]
l += l
d = [sum(i) for i in permutations(l,2) if sum(i) < 28124]
#print d[:50]
print sum(set(range(28124)) - set(d))
