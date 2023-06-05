from utilities.commands import info, status, help, hint, look
from utilities.commands import fly, take, talk, attack, shop, save


# Gets command from person playing te game
def get_command():
    return str(input("Enter command -> ")).strip()


# Prepears second word (argument) in command
def prepere_second_word(command):
    command2 = ''
    for word in command[1:]:
        command2 += word + ' '
    return command2.strip(' ')


'''
Interprets commands given by the player.
Performs specific functions for the selected command.
'''


def interpret(cmd, universe):
    print()
    if len(cmd) > 0:
        command = cmd.split()
    else:
        command = [None]
    cmd = cmd.lower()

    if cmd == "info":
        info(universe.get_player())

    elif cmd == "status":
        status(universe)

    elif cmd == "help":
        help()

    elif cmd == "hint":
        hint(universe._cMission)

    elif cmd == "look":
        look(universe)

    elif command[0] == "fly":
        fly(universe, prepere_second_word(command))

    elif command[0] == "take":
        take(universe, prepere_second_word(command))

    elif command[0] == "talk":
        talk(universe, prepere_second_word(command))

    elif command[0] == "attack" or command[0] == 'a':
        attack(universe, prepere_second_word(command))

    elif cmd == "shop":
        shop(universe)

    elif cmd == "save" or cmd == 's':
        save(universe)

    elif cmd == "exit" or cmd == 'e':
        return False

    else:
        print("Incorrect command!\nTry typing 'help'\n")

    # Checks if there are any itmes in player's inventory
    # that are required for mission and deletes item from required
    if universe._cMission is not None:
        for item in universe.get_player().get_items():
            if item.get_name() in universe._cMission.get_required():
                universe._cMission.delete_required(item.get_id())

    return True
