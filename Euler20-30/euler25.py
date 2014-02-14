def term_for_digit_length(y):
    a,b,x = 1,1,2
    while len(str(b)) < y:
        a,b = b, a+b
        x += 1
    print x
term_for_digit_length(1000)
                        
