def euler6(c):
    sum_of_square = sum(x**2 for x in range(c))
    square_of_sum = sum(x for x in range (c))**2
    print square_of_sum - sum_of_square
euler6(101)

#or

print sum(i for i in range(1,101))**2 -sum(i**2 for i in range(1,101))

