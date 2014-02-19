import sys,time,itertools
def divisors(x):
    l = set()
    for i in range(1,int(x**0.5) + 1):
        if not x % i:
            l.add(i)
            l.add(x / i)
    return sorted(list(l))
def makepandig(x,y,z):
    a = sorted(map(int,list(str(x) + str(y) + str(z))))
    print a
    if a == range(1,10):
        return True
    return False
l = set()
for i in xrange(10000):
    for a in divisors(i):
        for b in divisors(i):
            if a * b == i:
                if makepandig(a,b,i):
                    l.add(i)
print sum(l)
