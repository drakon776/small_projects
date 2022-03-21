'''
This is one of the simple python projects yet an exciting one.
You can even call it a mini-game. Make a program in which the computer randomly chooses a number
between 1 to 10, 1 to 100, or any range. Then give users a hint to guess the number.
Every time the user guesses wrong, he gets another clue, and his score gets reduced.
The clue can be multiples, divisible, greater or smaller, or a combination of all.
'''
from random import randint

number = int(input("Guess a Number in range 0-100:"))
mystery_number = randint(0,100)
while True:
    if number < mystery_number:
        print("Little higher")
        number = int(input("Try again: "))
    elif number > mystery_number:
        print("Little lower")
        number = int(input("Try again: "))
    elif number == mystery_number:
        print("You got it! BRAVO!")
        break



