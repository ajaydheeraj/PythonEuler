from primesieve import *
pri = sieve(10000)
def uallp(x,y,z):
    if ''.join(sorted(str(x))) == ''.join(sorted(str(y))) == ''.join(sorted(str(z))):
        return True
    return False
f = False
for i in pri[400:]:
    for n in range(2,5000,2):
        x = i
        y = (x + n)
        z = (y + n)
        if y in pri and z in pri and uallp(x,y,z) and len(str(y)) == 4 and len(str(z)) == 4:
            print str(x) + str(y) + str(z)
            f = True
            break
    if f:
        break

print uallp(1487,4817,8147)
