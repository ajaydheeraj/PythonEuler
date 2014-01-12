for a in range(500):
    for b in range(1000-a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2 and a < b < c:
            print a*b*c
            break
                

