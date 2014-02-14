tri = set((i * (i + 1)) / 2 for i in range(1,100))

l = {chr(96+i):i for i in range(1,27)}

def gtv(x):
    return sum(l[i.lower()] for i in x)

z = file("words.txt").read()
z = z.split('","')
z[0] = z[0][1:]
z[-1] = z[-1][:-1]

print sum(1 for i in z if gtv(i) in tri)
