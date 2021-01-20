from random import choice

def greet():
    with open('words.txt', encoding='utf8') as file:
        words = file.readlines()

    word = choice(words)
    word = word.strip()
    word = word.capitalize()

    if (word[-1] == 'd'):
        word = word[:-1] + 't'
    elif (not is_vowel(word[-1]) and word[-1] != 't'):
        word += 't'

    return word + " välkommen!"

def is_vowel(c):
    return c in 'aouåeiyäö'