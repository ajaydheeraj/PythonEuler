#Which starting number, under one million, produces the longest chain(Collatz)
#Rules: n --> n / 2 if n % 2 == 0, n --> 3n +1 if n % 2 != 0
colDict = {1:0}
maxLength = 0
maxInd = 0
def chainLength(x):
    if x in colDict:
        return colDict[x]
    colDict[x] = 1 + chainLength(3*x + 1 if x % 2 else x /2)
    return colDict[x]
print reduce(lambda x,y: x if chainLength(x) > chainLength(y) else y, range(500001,1000000,2),1)


'''
for i in range(500001,100000,2):
    c = chainLength(i)
    if c > maxLength:
        maxLength = c
        maxInd = i

print maxInd
'''


