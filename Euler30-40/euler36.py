def dtb(n):
    n = int(str(bin(n))[2:])
    return n

#ugly little one liner

print (sum(i for i in xrange(1,1000000) if str(i)[::-1] == str(i) and str(dtb(i))[::-1] == str(dtb(i))))

# same thing with indentation and nested if statement to make lines look better although its slower...

# count = 0
# for i in xrange(1,1000000):
#     if str(i)[::-1] == str(i):
#         if str(dtb(i))[::-1] == str(dtb(i)):
#                count += i
# print count
    
                        
