'''
As the name of the program suggests, we will be imitating a rolling dice.
This is one of the interesting python projects and will generate a random number each dice the program runs,
and the users can use the dice repeatedly for as long as he wants. When the user rolls the dice,
the program will generate a random number between 1 and 6 (as on a standard dice).

The number will then be displayed to the user. It will also ask users if they would like to roll the dice again.
The program should also include a function that can randomly grab a number within 1 to 6 and print it.
This beginner-level python projects will help build a strong foundation for fundamental programming concepts.

idea from https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/
'''

from random import randint

while True:
    num_dies = int(input("How many dice You wan\'t to roll?: "))
    num_kx = int(input("How many sides You wan\'t in die? "))

    for num in range(1, num_dies + 1):
        print(f"{num} die roll for:{randint(1, num_kx)}")

    if input("You want to roll again? y/n") == 'n':
        break
