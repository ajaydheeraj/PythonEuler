l = []
for a in range(2,101):
    for b in range(2,101):
        l.append(a ** b)
print len(set(l))

# print len(set(a ** b for a in range(2,101) for b in range(2,101)))
