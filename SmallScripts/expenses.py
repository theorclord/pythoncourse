expenses = [10.60,8,5,15,20,5,3]

sumList = 0
total = sum(expenses)

for ex in expenses:
    sumList = sumList + ex

print("You spent $", total, " on lunch this week.", sep="")


for i in range(7):
    print(i)