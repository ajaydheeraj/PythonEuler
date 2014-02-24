from gcdlcm import *
'''Prime factorizing all the numbers from 1 to 10 yield...
1 x 2 x 3 x 2^2 x 5 x 2 x 3 x 7 x 2^3 x 3^2 x 2 x 5
From 10 to 20 yield 11, 2^2 x 3 ,13, 2 x 7 ,5 x 3 , 2^4, 17,3^2 x 2, 19, and 2^2 x 5
Simplifying 1 to 10 yields(2^8 x 3^4 x 5^2 x 7)
we must multiply the highest power of each number and seeing as how these numbers are larger, the prime factorizations will be greatest for the numbers 10-20, 2^4 x 3 ^2 x 5 x 7 x 11 x 13 x 17 x 19''' 
print 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19 #this is the lcm


# OR

count = 1
for i in range(1,21):
    count = lcm(count,i+1) #increment the lcm
print count

# My personal favorite

print reduce(lcm,range(1,20)) #apply lcm to first and second element, second and third, so forth.
