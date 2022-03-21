'''
This is more of a “guess the word” game. The core concepts you have to use while developing this project are variables,
random, integer, strings, char, input and output, and boolean. In the game, users have to enter letter guesses,
and each user will have a limited number of guesses (a counter variable is needed for limiting the guesses).
This is one of the interesting python projects to begin with.

You can create a pre-organized list of words that users can grab words from. Also, you must include specific functions
to check whether or not a user has entered a single letter or if the input letter is in the hidden word,
to if the user has actually inputted a single letter, and to print the correct outcomes (letters).

idea from https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/
'''
from random import randint

hangman_pic = ['''
+---+
    |
    |
    |
   ===''', '''
+---+
O   |
    |
    |
   ===''', '''
+---+
O   |
|   |
    |
   ===''', '''
+---+
 O   |
/|   |
     |
    ===''', '''
+---+
 O   |
/|\  |
     |
    ===''', '''
+---+
 O   |
/|\  |
/    |
    ===''', '''
+---+
 O   |
/|\  |
/ \  |
    ===''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret ' \
        'fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newtotter owl panda parrot pigeon' \
        'python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad ' \
        'trout turkey turtle weasel whale wolf wombat zebra'.split()

word = words[randint(0, len(words) - 1)]
limit = 0
answer = list(len(word) * '_')
print(word)
print("Wecome in Hangman game :)\nYou have 7 tries to guess the answer.")
while True:

    counter = 0
    letter = input("Type a letter: ")

    for let in word:
        if letter == let:
            print("Excellent!")
            answer[counter] = letter

        elif letter not in word:
            print(":( Try again:")
            print(hangman_pic[limit])
            limit += 1
            break
        counter += 1

    if ''.join(answer) == word:
        print("You Win!!")
        break

    elif limit == 7:
        print("You Lose!")
        break
    print(answer)
