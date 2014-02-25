def divisors2(x):
    s = set()
    for i in range(1,int(x**0.5)+1):
        if not x % i:
            s.add(i)
            s.add(x//i)
    return sorted(list(s))

