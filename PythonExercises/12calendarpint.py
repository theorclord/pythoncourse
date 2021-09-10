import calendar

month = int(input("Month: "))
y = int(input("Year: "))

c = calendar.month(y, month)

print(c)