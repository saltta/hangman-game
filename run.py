import random


class Color:
    """
    Sets colors to be called for different texts.
    """
    RESET = '\033[0m'
    BLUE = '\u001b[34m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\u001b[33m'


def new_word():
    """
    Randomly selects a word from words.txt file
    so that every new round has a new word to be guessed.
    """
    with open('words.txt', 'r') as h:
        words = h.readlines()
    random_word = random.choice(words)[:-1].upper()
    return random_word


def title_screen():
    """
    Introduces the player to the game.
    Gives them the option to start right away or read the instructions first.
    """
    word = new_word()
    title_graphic()
    print(hangman_graphics(0))
    print(f"Type {Color.BLUE}1 {Color.RESET}to begin the game\n")
    print(f"Type {Color.BLUE}2 {Color.RESET} to read the instructions")
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
            print(f"\n{Color.YELLOW}Please type {Color.BLUE}1 {Color.YELLOW}or"
                  f"{Color.BLUE} 2 {Color.YELLOW}to make your choice."
                  f"{Color.RESET}")


def instructions():
    """
    Displays instructions for playing the game.
    """
    print(
        """
        Try to guess the word by typing 1 individual letter at a time.
        Every wrong letter attempt will cost you 1 chance
        and the hanging of the poor man will begin!
        Once you run out of chances the man will be hanged!
        Save him by guessing the correct letters before your chances reach 0.
        Be smart or the man will perish.
        Good luck!
        """
    )
    start = input("Press the enter key to return to the title screen.\n")
    title_screen()


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
        guess = input("Try a letter:\n").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(Color.YELLOW + f"\nYou have already tried {guess}!\n" +
                      Color.RESET)
            elif guess not in word:
                print(Color.YELLOW + f"\nOh no! {guess} isn't in the word!\n" +
                      Color.RESET)
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
        win_graphic()
        print("Great job! You guessed the word and saved the poor man!")
        print("My hero!")
    else:
        lose_graphic()
        print("Aw, I feel sorry for that guy, but at least you tried.")
        print(f"The word was: {word}.")
    restart_game()


def restart_game():
    """
    Asks if the player wants to restart the game.
    If not, returns to title screen.
    """
    restart_choice = input("\nWant to go another round? Y/N\n").upper()
    if restart_choice == "Y":
        word = new_word()
        start_game(word)
    elif restart_choice == "N":
        title_screen()
    else:
        print(f"You have to choose Y or N. You chose {restart_choice}.\n")
        restart_game()


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


def title_graphic():
    """
    A title graphic to be displayed on the title screen.
    """
    print(
        """
        ░░   ░░  ░░░░░  ░░░    ░░  ░░░░░░  ░░░    ░░░  ░░░░░  ░░░    ░░
        ▒▒   ▒▒ ▒▒   ▒▒ ▒▒▒▒   ▒▒ ▒▒       ▒▒▒▒  ▒▒▒▒ ▒▒   ▒▒ ▒▒▒▒   ▒▒
        ▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒ ▒▒ ▒▒  ▒▒ ▒▒   ▒▒▒ ▒▒ ▒▒▒▒ ▒▒ ▒▒▒▒▒▒▒ ▒▒ ▒▒  ▒▒
        ▓▓   ▓▓ ▓▓   ▓▓ ▓▓  ▓▓ ▓▓ ▓▓    ▓▓ ▓▓  ▓▓  ▓▓ ▓▓   ▓▓ ▓▓  ▓▓ ▓▓
        ██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████
        """
    )


def win_graphic():
    """
    Displays a win graphic for when the player correctly guesses the word.
    """
    print(Color.GREEN +
          """
           ___       __   ___  ________
          |\\  \\     |\\  \\|\\  \\|\\   ___  \\
          \\ \\  \\    \\ \\  \\ \\  \\ \\  \\\\ \\  \\
           \\ \\  \\  __\\ \\  \\ \\  \\ \\  \\\\ \\  \\
            \\ \\  \\|\\__\\_\\  \\ \\  \\ \\  \\\\ \\  \\
             \\ \\____________\\ \\__\\ \\__\\\\ \\__\\
              \\|____________|\\|__|\\|__| \\|__|
        """ + Color.RESET
          )


def lose_graphic():
    """
    Displays a lose graphic for when the player fails to guess the word.
    """
    print(Color.RED +
          """
           ________ ________  ___  ___
          |\\  _____\\\\   __  \\|\\  \\|\\  \\
          \\ \\  \\__/\\ \\  \\|\\  \\ \\  \\ \\  \\
           \\ \\   __\\\\ \\   __  \\ \\  \\ \\  \\
            \\ \\  \\_| \\ \\  \\ \\  \\ \\  \\ \\  \\____
             \\ \\__\\   \\ \\__\\ \\__\\ \\__\\ \\_______\\
              \\|__|    \\|__|\\|__|\\|__|\\|_______|
        """ + Color.RESET
          )


title_screen()
