def euler4():
    l = []
    for i in range(900,1000):
        for x in range(1000,900,-1):
            if str(i*x) == str(i*x)[::-1]:
                l.append(i*x)
    return l[-1]
print euler4()         
            
