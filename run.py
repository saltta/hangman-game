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
    while not endgame and chances > 0:
        guess = input("Guess as letter:\n").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already tried the letter", guess)
                


start_game(word)
