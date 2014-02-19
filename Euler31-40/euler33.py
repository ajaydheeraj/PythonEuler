from __future__ import division
def fair_game(x,y):
    if '0' in list(str(x)) or '0' in list(str(y)):
        return False
    if x / y > 1:
        return False
    if x == y:
        return False
    x0 = set(list(str(x)))
    y0 = set(list(str(y)))
    if len(x0.intersection(y0)) != 1:
        return False
    return True
print fair_game(49,98)
def bad_division(x,y):
    x1 = map(int,list(str(x)))
    y2 = map(int,list(str(y)))
    for i in x1:
        for a in y2:
            if i == a:
                x1.remove(i)
                y2.remove(a)
    for j in x1:
        for h in y2:
            return j/h
def gcd(a,b):
    return gcd(b,a%b) if a % b else b

num = 1
denom = 1
for a in range(10,100):
    for b in range(10,100):
        if fair_game(a,b):
            if bad_division(a,b) == a /b:
                num *= a
                denom *= b
print num / gcd(num,denom)
print denom / gcd(num, denom)
