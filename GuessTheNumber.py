import random

number = random.randint(1, 20)
Guesses = 9
print('''
Game Instructions :
A random number between the range of 1 to 20 is hidden you have to guess that number. 
You have 9 chances. 
If you will be unable to guess that number in 9 chances the game will be overed. 
Best Luck to you
''')
try:
    while Guesses != 0:
        print("Chances left : " + str(Guesses))
        Guess = int(input())
        if Guess == number:
            print("You Won, Congratulation!")
            break
        elif Guess > number:
            print("Number is smaller than your input")
            Guesses = Guesses - 1
        elif Guess < number:
            print("Number is greater than your input")
            Guesses = Guesses - 1
        else:
            print("You Won, Congratulation!")
            break
except Exception as e:
    print(e)
    print("You have to enter number not String")
if Guesses == 0:
    print("You don't have enough guesses left")
    print("the number was " + str(number))
    print("Game Over")
