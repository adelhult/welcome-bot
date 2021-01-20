from random import choice

def greet():
    with open('words.txt', encoding='utf8') as file:
        words = file.readlines()

    word = choice(words)
    word = word.strip()
    word = word.capitalize()
    if (word[-1] == 'd'):
        word = word[:-1] + 't'
    elif (not(isVowel(word[-1])) and word[-1] != 't'):
        word += 't'

    phrase = word + " välkommen!"
    return phrase

def isVowel(c):
    isVowel = (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u')
    return isVowel
    