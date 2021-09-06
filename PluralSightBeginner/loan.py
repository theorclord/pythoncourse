# Get the loan details
moneyOwed = float(input("How much money do you owe, in gold?\n")) # ex 250gp
apr = float(input("What is the annual percentage rate?\n")) # 3
payment = float(input("What will your monthly payment be, in gold?\n")) # 25gp
months = int(input("How many months do you want to see the results for?\n")) # 10

# Divide apr by 100 to make it a percent, then divide by 12 to make it monthly
monthlyRate = apr/100/12

for i in range(months):
    # Add in interest
    interestPaid = moneyOwed * monthlyRate
    moneyOwed = moneyOwed + interestPaid
    
    if(moneyOwed - payment < 0):
        print("The last payment is", moneyOwed)
        print("You paid off the loan in", i+1, "months")
        break

    # Make Payment
    moneyOwed = moneyOwed - payment

    # Print the results after this month
    print("Paid", payment, "of which", interestPaid, "was interest", end=' ')
    print("Now I owe", moneyOwed)