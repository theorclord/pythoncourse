import random as ran

computerChoice = ran.choice(['scissors','rock','paper'])

userChoice = input('Do you want - rock, paper, or scissors?\n')

if computerChoice == userChoice:
    print('Tie')
elif userChoice == 'rock' and computerChoice == 'scissors':
    print('You win!, the computer had ' + computerChoice)
elif userChoice == 'paper' and computerChoice == 'rock':
    print('You win!, the computer had ' + computerChoice)
elif userChoice == 'scissors' and computerChoice == 'paper':
    print('You win!, the computer had ' + computerChoice)
else:
    print('Computer wins!, the computer had ' + computerChoice)
