count = 0
for i in range(2,354294):
    if sum(int(y)**5 for y in str(i)) == i:
        count += i
print count
# print sum(i for i in range(2,1000000) if sum(int(y) ** 5 for y in str(i)) == i)
