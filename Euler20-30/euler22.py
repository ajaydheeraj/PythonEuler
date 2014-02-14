x = open("euler22.txt", "r")
x = x.read()
x = x.split('","')
x[0] = x[0][1:]
print x
x[-1] = x[-1][:-1]
x = sorted(x)

pv = {}
s = ord("A")
for i in range(0,26):
    pv[chr(s+i)] = i + 1

sum = 0
for i in x:
    for a in i:
        sum += (x.index(i) + 1) * pv[a]
print sum
