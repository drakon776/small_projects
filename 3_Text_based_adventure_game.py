"""
This is a basic version of the Adventure game. It is completely text-based. In this version of the game,
users can move about through different rooms within a single setting, and based on the user input,
it will provide descriptions for each room. This is one of the interesting python projects.
Movement direction is crucial here – you must create walls and set the directions in which the users can move
through the rooms, set movement restrictions, and also include a tracker that can track how far a user has walked
or moved in the game. Mentioning Python projects can help your resume look much more interesting than others.

idea from https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/
"""
from random import randint

# descriptions will be completed soon :)
name = input('Please, tell me your name: ')
locations = ['The Room', 'Room 1', 'Room 2', 'Room 3', 'exit']
events = ['--1--', '--2--', '--3--', '--4--', '--5--', '--6--', '--7--', '--8--']
num = 0
commands = ['go', 'stay', 'back']
print(
    f'Hi {name} and welcome. You are in --{locations[num]}--. '
    f'What You want do do? \ngo - go out\nstay - search your surrounding\nback - go back ')
while True:
    luck = randint(0,1)
    choice = input()
    if choice == 'go':
        print(f'you move to --{locations[num + 1]}--')
        num += 1
        if luck == 1:
            print(f'{events[randint(0, len(events)-1)]} happend.')

    elif choice == 'stay':
        print(f'you look around --{locations[num]}-- and {events[randint(0, len(events)-1)]} happend.')

    elif choice == 'back':
        if num == 0:
            print(f'you left {locations[0]}. \nGAME OVER')
            break
        num -= 1
        print(f'you back in {locations[num]}')
        if luck == 1:
            print(f'{events[randint(0, len(events)-1)]} happend.')

    elif choice not in commands:
        print(f'Please write again :)')

    if locations[num] == 'exit':
        print(f'You left last location.\nYou WIN!')
        break
