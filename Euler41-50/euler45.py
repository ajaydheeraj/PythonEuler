def tri(x):
    return (x * (x + 1)) / 2
def pent(x):
    return ( x * (3 * x - 1)) / 2
def hex(x):
    return (x * (2 * x - 1))
hex1 = set(hex(x) for x in range(100000))
pent1 = set(pent(x) for x in range(100000))
tri1 = set(tri(x) for x in range(100000))
for i in range(40756,100000):
    t = tri(i)
    if t in hex1 and t in pent1:
        print t
