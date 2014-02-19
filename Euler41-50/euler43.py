from itertools import permutations
def ispandig(x):
    if len(str(x)) != 10:
        return False
    x1 = sorted([int(i) for i in str(x)])
    if  x1 == range(10):
        return True
    return False
def substring(x):
    d = [2,3,5,7,11,13,17]
    for i in range(1,8):
        if int(str(x)[i:i+3]) % d[i-1]:
            return False
    return True
k = list(permutations([0,1,2,3,4,5,6,7,8,9]))
l = []
for i in k:
    l.append(int(''.join(str(c) for c in i)))
print sum(i for i in l if substring(i))
