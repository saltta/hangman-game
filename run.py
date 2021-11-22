import random

with open('words.txt', 'r') as h:
    words = h.readlines()

word = random.choice(words)[:-1].upper()


def start_game(word):
    """
    Starts the game.
    """
    secret_word = "_" * len(word)
    endgame = False
    guessed_letters = []
    chances = 6
    print("Let's play Hangman!\n")
    print(f"Chances left: {chances}\n")
    print("Guess this word: " + " ".join(secret_word) + "\n")


start_game(word)
