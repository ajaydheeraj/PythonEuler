def sum_under_term(x):
    
    a,b,s = 1,1, 0
    while b < x:
        if b % 2 == 0:
            s += b
        a,b = b, a+b
    print s

sum_under_term(4000000)
