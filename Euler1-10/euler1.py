# Euler 1: Find the sum of all the multiples of 3 or 5 below 1000.
count=0
for i in range(1000):
    if (i%3==0) or (i%5==0): # if i divides into 3 evenly or 5 evenly
        count+=i #add it to the count
print count #print the count
#print the sum of i in range(1000) if i % 3 is false(0) or i % 5
print sum(i for i in range(1000) if not i % 3 or not i % 5)


