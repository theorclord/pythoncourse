import datetime

d1 = (2014, 7, 2)
d2 = (2014, 7, 11)

date1 = datetime.datetime(d1[0],d1[1],d1[2])
date2 = datetime.datetime(d2[0],d2[1],d2[2])

d3 = date1-date2

print(date1)