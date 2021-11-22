import random

with open('words.txt', 'r') as h:
    words = h.readlines()

word = random.choice(words)[:-1]
