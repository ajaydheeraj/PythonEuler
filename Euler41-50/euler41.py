import primesieve

d = primesieve.sieve(7654322)
x = list(d)

for i in reversed(x):
    i = [int(y) for y in str(i) if len(str(i)) == 7]
    if len(i) == (len(set(i))):
        if sorted(i) == range(1,8):
            print ''.join(map(str,i))
            break
            
