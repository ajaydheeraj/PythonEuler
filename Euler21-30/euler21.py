def sdivisors(x):
    y = set(reduce(list.__add__, ([i,x//i] for i in range(1,int(x**0.5) + 1) if not x % i)))
    y.remove(x)
    return sum(y)

a, c = 2,[]
while a < 10000:
    if sdivisors(sdivisors(a)) == a and a != sdivisors(a):
        c.append(a)
        c.append(sdivisors(a))
    a += 1
print sum(set(c))



    
