def findsol(p):
    l = []
    for a in range(1,p):
        for b in range(1,p-a):
            c= p - a - b
            if a ** 2 + b ** 2 == c**2:
                l += [a,b,c] #add the triple
    return len(l) / 6 # length of the list / 3 for the triple / 2 for doubles
print max( (j-1) * 120 for j in (findsol(p) for p in range(0,1000,120)))
# -1 to account for list position, times 120 because of the range 
