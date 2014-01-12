def sum_under_term(x):
    
    a,b,s = 1,1, 0
    while b < x:
        if b % 2 == 0:
            s += b
        a,b = b, a+b
    print s

sum_under_term(4000000)

def term_for_digit_length(y):
    a,b,x = 1,1,2
    while len(str(b)) < y:
        a,b = b, a+b
        x += 1
    else:
        print x 
          
term_for_digit_length(1000)
        
