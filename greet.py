from random import choice

def greet():
    with open('words.txt') as file:
        words = file.readlines()

    word = choice(words)
    
    return f"{word}  välkommen!"