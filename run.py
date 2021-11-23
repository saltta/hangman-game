import random

with open('words.txt', 'r') as h:
    words = h.readlines()

word = random.choice(words)[:-1].upper()


def title_screen():
    """
    Introduces the player to the game.
    Gives them the option to start right away or read the instructions first.
    """
    print("Type 1 to begin the game\n")
    print("Type 2 to read the instructions")
    selection = False
    while not selection:
        choice = input(" \n")
        if choice == "1":
            selection = True
            start_game(word)
        elif choice == "2":
            selection = True
            instructions()
        else:
            print("Please type 1 or 2 to make your choice.")


def instructions():
    """
    Displays instructions for playing the game.
    """
    print(
        """
        Try to guess the word by typing in individual letters.
        Every wrong letter attempt will cost you one chance
        and the hanging of the poor man will begin!
        Once you run out of chances the man will be hanged!
        Save him by guessing the correct letters before your chances reach 0.
        Be smart or the man will perish.
        Good luck!
        """
    )
    start = input("Press the enter key to start the game.\n")
    start_game(word)


def start_game(word):
    """
    Starts the game.
    """
    secret_word = "_" * len(word)
    endgame = False
    guessed_letters = []
    chances = 6
    print("Save the man from hanging!\n")
    print(f"Chances left: {chances}\n")
    print("Guess this word: " + " ".join(secret_word) + "\n")
    print(hangman_graphics(chances))
    while not endgame and chances > 0:
        guess = input("Guess a letter:\n").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"\nYou have already tried {guess}!\n")
            elif guess not in word:
                print(f"\nOh no! {guess} isn't in the word!\n")
                chances -= 1
                guessed_letters.append(guess)
            else:
                print(f"\nNice! {guess} is in the word!\n")
                guessed_letters.append(guess)
                word_as_list = list(secret_word)
                indices = [i for i, letter in enumerate(word)
                           if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                secret_word = "".join(word_as_list)
                if "_" not in secret_word:
                    endgame = True
        elif len(guess) != 1:
            print("\nUh oh, you have to guess 1 letter at a time.")
            print(f"You used {len(guess)} characters.\n")
        else:
            print("\nWhat are you doing? You can only guess letters!")
            print(f"{guess} is not a letter!\n")
        print(hangman_graphics(chances))
        print(f"Chances left: {chances}\n")
        print("Guess this word: " + " ".join(secret_word) + "\n")
        print("Letters tried: " + ", ".join(guessed_letters) + "\n")
    if endgame:
        print("Great job! You guessed the word and saved the poor man!")
        print("My hero!")
    else:
        print("Aw, I feel sorry for that guy, but at least you tried.")
        print(f"The word was: {word}.")


def hangman_graphics(chances):
    """
    Visual representation for how many chances the player has left.
    """
    hanging_steps = [
        """
              =======
              |/    |
              |     @
              |    /|\\
              |     |
              |    / \\
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """,
        """
              =======
              |/    |
              |     @
              |    /|\\
              |     |
              |    /
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """,
        """
              =======
              |/    |
              |     @
              |    /|\\
              |     |
              |
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """,
        """
              =======
              |/    |
              |     @
              |    /|
              |     |
              |
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """,
        """
              =======
              |/    |
              |     @
              |     |
              |     |
              |
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """,
        """
              =======
              |/    |
              |     @
              |
              |
              |
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """,
        """
              =======
              |/    |
              |
              |
              |
              |
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """
    ]
    return hanging_steps[chances]


title_screen()
