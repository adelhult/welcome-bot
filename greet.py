from random import choice
from discord import File

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

def get_gif():
    gif_list = ['welcome1.gif', 'welcome2.gif', 'welcome3.gif', 'welcome4.gif', 'welcome5.gif']
    gif = choice(gif_list)
    
    with open('welcomes/' + gif, 'rb') as f:
        return File(f, filename='welcome.gif')
    
def is_vowel(c):
    return c in 'aouåeiyäö'
