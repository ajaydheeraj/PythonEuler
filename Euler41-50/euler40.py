irrational = "0.1"
i = 2
while len(str(irrational)) < 1000003:
    irrational += str(i)
    i += 1
# print irrational
print int(irrational[2]) * int(irrational[11]) * int(irrational[101]) * int(irrational[1001]) * int(irrational[10001]) * int(irrational[100001]) * int(irrational[1000001])
