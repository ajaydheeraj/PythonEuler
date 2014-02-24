def sum_under_term(x):
    a,b,s = 1,1, 0 #first term, second term, sum
    while b < x: 
        if not b % 2 : #if even
            s += b #add it to the sum
        a,b = b, a+b #tuple unpacking! way better than temp = a; a = b; b = b += temp
    return s # gimme the sum

print sum_under_term(4000000)
