import calendar
'''
count = 0

month= 1
year = 1901
while year < 2001:
    if calendar.weekday(year,month,1) == 6:
        count +=1
    month +=1
    if month == 13:
        year += 1
        month = 1
print count
'''
count = 0
for year in range(1901,2001):
    for month in range(1,13):
        if calendar.weekday(year,month,1) == 6:
            count +=1
print count
