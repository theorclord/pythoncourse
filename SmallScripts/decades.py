age = int( input("How old are you?\n"))

decades = age // 10
yearsRemaing = age % 10

print("You are " + str(decades) + " decades and " + str(yearsRemaing) + " years old.")