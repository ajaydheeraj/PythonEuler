x = open("euler22.txt", "r")
x = x.read()
x = x.split('","')
x[0] = x[0][1:]
x[-1] = x[-1][:-1]
x = sorted(x)

l = {chr(64+i):i for i in range(1,27)}
print sum((x.index(i) + 1) * l[a] for i in x for a in i)
