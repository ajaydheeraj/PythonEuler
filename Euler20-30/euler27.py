import primesieve
p = primesieve.sieve(100000)
def plugin(a,b):
    count = 0
    n = 0
    while n**2 + a * n + b in p:
        count +=1
        n +=1
    return count
print plugin(-79,1601)
d = []
tc = 0
for a in range(-999,1000,2):
    for b in p:
        if plugin(a,b) > tc:
            tc = plugin(a,b)
            d.append(a * b)
print d
