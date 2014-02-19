import primesieve

y  = set(primesieve.sieve(1000000))

def trunc(x):
    x = str(x)
    t = len(x) - 1
    m = 0
    while t >= 1:
        if int(x[0:t]) in y:
            t -= 1
        else:
            return False
    while m <= len(x) - 1:
        if int(x[m:]) in y:
            m += 1
        else:
            return False
    return True
print sum(i for i in y if trunc(i) and len(str(i)) > 1)


def trunc2(x):
    d = str(x)
    for i in range(len(d)):
        if int(d[i:]) not in y:
            return False
    for i in range(len(d),0,-1):
        if int(d[:i]) not in y:
            return False
    return True
# count = 0
# summy = 0
# while count < 11:
#     for i in y[20:]:
#         if trunc2(i):
#             summy += i
#             count += 1
#             print str(i) + 'is a solution'
