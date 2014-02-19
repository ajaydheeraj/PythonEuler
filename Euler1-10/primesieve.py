def sieve(n): # all primes under number
    l = [True] * (n+1) # set up grid
    l[0] = l[1] = False# mark 0 and 1 as not prime
    for i in xrange(2,int(n**0.5)+1):# loop up to the sqrt of n
        if l[i]:#if l[i] is true
            for a in xrange(i*i,n+1,i):#all remaining increments of i
                l[a] = False#mark them all false
    return [i for i,j in enumerate(l) if j]# return the values of the prime numbers

