# 05 : HANGMAN WORD GUESSING

# In this pyhthon project we will learn how to work with dictionaries, lists, and 
# nested if statements. You will also learn how to work with the string and random
# Python modules.

import random
import string
from words import words

def get_valid_words(words):
    word = random.choice(words)  
    while '_' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_words(words)
    word_letters = set(word) 
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print('\nYou have', lives, 'lives left and you have used these letters :', ' '.join(used_letters) + " 🧠")

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current Words: ", ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1  
                print("Letter is not in word. 💀")

        elif user_letter in used_letters:
            print("You have already used that character. Please try again. 🔄")

        else:
            print("Invalid character. Please try again. 🚫")

    if lives == 0:
        print("You died, sorry. The word was", word, "💀👻")
    else:
        print("Congratulations! You've guessed the word! 🎉")

hangman()