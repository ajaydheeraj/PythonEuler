from num2words import num2words
count = 0
for i in range(1,41):
    x = num2words(i)
    x = x.replace(",","and")
    x = x.replace("-","")
    x = x.replace(" ", "")
    print x
    count += len(x)
    print count
print count
    
    
