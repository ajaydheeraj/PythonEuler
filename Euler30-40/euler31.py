import time
# l = [ range(0,201,200), range(0,201,100), range(0,201,50), range(0,201,20), range(0,201,10), range(0,201,5), range(0,201,2), range(0,201,1)]
# print l
# count = 0
# for a in l[0]:
#     for b in l[1]:
#         for c in l[2]:
#             for d in l[3]:
#                 for e in l[4]:
#                     for f in l[5]:
#                         for g in l[6]:
#                             for h in l[7]:
#                                 if a + b + c + d + e + f + g + h == 200:
#                                     count += 1
# print count
count = 1
#for a in range(200,-1,-200):
for b in range(200,-1,-100):
    for c in range(b,-1,-50):
        for d in range(c,-1,-20):
            for e in range(d,-1,-10):
                for f in range(e,-1,-5):
                    for g in range(f,-1,-2):
                        count += 1
print count
