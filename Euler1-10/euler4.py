def euler4():
    l = [] #list of palindromes
    for i in range(900,1000): #started higher up
        for x in range(1000,900,-1): #going reversed
            if str(i*x) == str(i*x)[::-1]: #if the string is the same reversed
                l.append(i*x) #add it to the list
    return sorted(l)[-1] # sort it, print the last element
print euler4()         
            
