import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word =  random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    user_letter = input("guess a letter: ".uppper())
    if user_letter in alphabet 
