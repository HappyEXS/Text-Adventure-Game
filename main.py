from utilities.game_start import start_game, create_game, load_game
from utilities.interpret import interpret, get_command
from utilities.additional_func import delete_mission, show_credits
from utilities.commands import introduction


def main():
    # Performs start game procdures
    if start_game():
        universe = create_game()
        print(universe._player.get_name() + " welcome in the game!!!\n")
    else:
        universe = load_game()
        print(universe._player.get_name() + " welcome back in the game!!!\n")

    # Prints intruduction to the game
    introduction(universe)

    # Main loop. Game ends when gameEnd is True
    gameEnd = False
    while not gameEnd:
        # Updates planet and mission
        cPlanet, cMission = universe.get_current_Planet_Mission()

        # Deletes mission when completed
        if cMission is not None and cMission.check_if_done():
            delete_mission(universe)

        # When all missions are completed ends the game
        if universe.end_of_game():
            show_credits(universe.get_player())
            gameEnd = True

        # Takes command from user
        command = get_command()
        # When interpreting command returns False ends the game
        if not interpret(command, universe) and gameEnd is False:
            gameEnd = True
            continue


if __name__ == '__main__':
    main()
