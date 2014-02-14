increment = 2
count = 0
i = 1
tot = 0
while i < (1001 * 1001) + 1:
    tot += i
    i += increment
    count += 1
    if not count % 4:
        increment += 2
print tot
