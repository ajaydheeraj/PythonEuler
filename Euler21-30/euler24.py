from itertools import permutations

x = list(permutations([0,1,2,3,4,5,6,7,8,9]))[999999]
print int(''.join(str(i) for i in x))
