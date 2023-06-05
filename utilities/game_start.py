from utilities.file_data import TITLE, DEFAULT_GAME, SAVE, LOAD
from classes.world import World
import json


# Shows game title. Returns what choose mode returns
def start_game():
    print('\n' + '#' * len(TITLE) * 2 + '\n')
    print(' ' * (len(TITLE) // 2) + TITLE)
    print('\n' + '#' * len(TITLE) * 2 + '\n')
    while (True):
        ifCraate = choose_mode()
        if ifCraate is not None:
            return ifCraate


# Returns True if user choses to start new game.
# Returns False if user choses to load game.
def choose_mode():
    print('Choose mode in which you want to start a game:')
    print(' 1. Create new game\n 2. Load saved game\n')

    try:
        startMode = int(input('Choose mode 1 or 2: '))
        if startMode == 1:
            return True
        elif startMode == 2:
            return False
        else:
            print('\nInvalid mode option, please try again\n')
            return None
    except ValueError:
        print('\nInvalid mode option, please try again\n')
        return None


# Creates new game from file
def create_game():
    name = str(input("\nWhat is your name adventurer?\nType your name: ")).strip()
    if len(name) < 1:
        print("Your name consist of only whitespaces. Input correct name!")
        create_game()

    try:
        with open(DEFAULT_GAME) as f:
            file = json.load(f)

            file["player"]["name"] = name

            universe = World(file)

    except (KeyError, ValueError):
        print("\n\t[Game could not be created. Given file is broken.]\n")
        print("\tCheck the file or create new game.")
        exit()
    except FileNotFoundError:
        print("\n\t[Given game file does not exist.]\n")
        exit()

    with open(SAVE, 'w') as f:
        json.dump(file, f)

    print("\n\t[New game created!] \n" + '_' * 50 + '\n')
    return universe


# Creates game from load file
def load_game():
    try:
        with open(LOAD) as f:
            file = json.load(f)
        try:
            universe = World(file)
            print("\n\t[Game loaded succesfully!] \n" + '_' * 50 + '\n')
            return universe
        except (KeyError, ValueError):
            print("\n\t[Game could not be loaded. Given file is broken.]\n")
            print("\tCheck the file or create new game.")
            exit()

    except FileNotFoundError:
        print("\n\t[Given load game file does not exist.]\n")
        userState = str(input('Do you want to create new game? [Y/n]: '))
        if userState.lower() == 'y' or userState.lower() == 'yes':
            return create_game()
        else:
            print("\nToo bad you don't want to play the game")
            print("Maybe next time :)")
            print("See You\n")
            exit()
