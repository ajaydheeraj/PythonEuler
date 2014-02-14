'''
count = 0
for i in range(1,1001):
    count += i ** i
print str(count)[-10:]
Explanation for code:
adding the number ** number to the count
converting it to a string
getting the digits from the 10th from the right, to the end
'''
print str(sum(i ** i for i in range(1,1001)))[-10:]

