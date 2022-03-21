'''
The program design is such that it will ask users to enter a series of inputs
that will be considered as a Mad Lib. Mab lib is one of the python projects for beginners.The input could be anything,
an adjective, a noun, a pronoun, etc. Once all the inputs are entered, the application will take the data and arrange
the inputs into a story template form. Sound fun, right?

idea from https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/
'''


def mad_lib_game():
    noun = input("\ntell me first noun: ")
    adj = input("tell me adjective: ")
    adj2 = input("tell me second adjective: ")

    print(f"{noun} are red\nVoilet are {adj}\nYou have to know I {adj2} for you\n")

    again = input('Do You wan\'t to play again? y/n: ')

    if again == 'y':
        mad_lib_game()

    else:
        print("\nThanks for playing :)")


mad_lib_game()
