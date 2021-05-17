number = 18
Guesses = 9
print('''
Game Instructions :
A number is hidden you have to guess that number. 
You have 9 chances. 
If you will be unable to guess that number in 9 chances the game will be overed. 
Best Luck to you
''')
while Guesses != 0:
    print("Chances left : " + str(Guesses))
    Guess = int(input())
    if Guess == 18:
        print("You Won, Congratulation!")
        break
    elif Guess > 18:
        print("Number is smaller than your input")
        Guesses = Guesses - 1
    elif Guess < 18:
        print("Number is greater than your input")
        Guesses = Guesses - 1
    else:
        print("You Won")
        break

if Guesses == 0:
    print("You don't have enough guesses left")
    print("the number was " + number)
    print("Game Over")
