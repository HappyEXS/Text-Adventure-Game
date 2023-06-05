from utilities.file_data import SAVE
from utilities.additional_func import duel2, generate_sentence
import json

'''
Functions performed by interpret function.
Every command entered has its own function.
'''


def info(player):
    print(player.__str__() + "\n")


def status(universe):
    currentPlanet, currentMission = universe.get_current_Planet_Mission()
    print(universe.get_player().show_stats())
    print("[Current mission on this planet]")
    if currentMission is None:
        print("You have finished all misions on this planet")
    else:
        print(currentMission)
    print()


def help():
    with open(SAVE) as f:
        file = json.load(f)
    print('_' * 70 + '\n')
    for text in file["help"]:
        print(text)
    print('_' * 70 + '\n')


def hint(mission):
    if mission:
        print(mission.hint() + '\n')
    else:
        print("You have finished all misions on this planet\n")


def look(universe):
    currentPlanet, currentMission = universe.get_current_Planet_Mission()
    location = universe.get_player().location()
    print("You are on " + location + ".\nYou can fly to nearby planets:")
    planetList = ''
    for planet in universe._map.available_paths(location):
        planetList += planet + ', '
    print(planetList[:-2] + '\n')
    if currentPlanet.if_store_on_planet():
        print(generate_sentence(currentPlanet.get_store().get_name(), "store") + '\n')
    if currentMission and not currentMission.check_if_done():
        print(currentMission.get_surroundings())
        print("[Mission status]:")
        print(currentMission.__str__() + "\n")
    else:
        print("You have finished all current misions on this planet.\n")


def fly(universe, planetName):
    player = universe.get_player()
    if planetName in universe._map.available_paths(player.location()):
        remaining_fuel = player.get_stat('fuel')
        if remaining_fuel < 20:
            print(f"Amount of gasoline in the tank: {remaining_fuel}")
            print("You don't have enought fuel to travel to another planet!\nInterplanetary journey burns 20 galons of fuel.\n")
        else:
            player.set_location(planetName)
            player.add_stat("fuel", -20)
            print(f"Ramaining fuel: {player.get_stat('fuel')}")
            info = f"Welcome to the {planetName}"
            print('#' * len(info) * 2 + '\n')
            print(' ' * (len(info) // 2) + info + '\n')
            print('#' * len(info) * 2)
            status(universe)

    elif planetName in universe._map._planetList:
        if planetName == player.location():
            print(f"You are currently on {planetName}.\n")
        else:
            print(f"{planetName} is too far away. You can't fly there from {player.location()}.\n")
    else:
        print("[Wrong planet name]")
        print(f"From {player.location()} you can fly to:")
        planetList = ''
        for planet in universe._map.available_paths(universe.get_player().location()):
            planetList += planet + ', '
        print(planetList[:-2] + '\n')


def take(universe, itemName):
    mission = universe._cMission
    if itemName in mission.get_items() or itemName in mission.get_required():
        item = mission.take_item(itemName)
        universe.get_player().pickup_item(item)
        print("You have picked up:")
        print(item)
    else:
        print("The given item can not be found. Input correct item name.\n")


def talk(universe, npcName):
    mission = universe._cMission
    if npcName in mission.get_npcs():
        npc = mission.get_npc_obj(npcName)
        print(npc)
        mission.delete_npc(npc.get_id())
    else:
        print("There is no one of such a name in the area.\n")


def attack(universe, enemyName):
    mission = universe._cMission
    if enemyName in mission.get_enemies():
        enemy = mission.get_enemy_obj(enemyName)
        if duel2(universe.get_player(), enemy) is True:
            mission.delete_enemy(enemy.get_id())
        else:
            # print("Unfortunately you have lost your fight.\nUpgrade your gear and face again your opponent.\n")
            print("No one died in the fight. Attack aagain to kill enemy!\n")
    else:
        print("There is no one of such a name in the area.\n")


def shop(universe):
    if universe._cPlanet.if_store_on_planet():
        store = universe._cPlanet.get_store()
        player = universe.get_player()
        print(f"Availabe gold in you pocket: {player.get_stat('gold')}")
        print(store)
        i = len(store.get_items_ids())
        in_store = True
        while in_store:
            choice = input("\nInput item number which you want to purchase or 'exit'/'e'\n -> ").strip()
            try:
                choice = int(choice) - 1
                if choice in range(0, i):
                    item = store.get_item(choice)
                    if player.get_stat("gold") >= item.get_price():
                        YesorNo = input(f"Do you want to buy {item.get_name()} for {item.get_price()} gold?\n Y/n: ")
                        if YesorNo.lower() == 'y':
                            player.buy_item(item)
                            print(f"You have bought {item.get_name()}!  Your balance: {player.get_stat('gold')}")
                        else:
                            continue
                    else:
                        print(f"This item is too expensive for you.  Your balance: {player.get_stat('gold')} gold.")
                else:
                    print("Sorry, you have choosen an unknown item. Please try again.")
            except ValueError:
                if choice.lower() == "exit" or choice.lower() == 'e':
                    print("You have left shop.\n")
                    in_store = False
                else:
                    print("Incorrect input")
    else:
        print("There is no store available on this planet.\n")


def save(universe):
    universe.save()
    print("Game saved succesfully.\n")


# Prints help and look command at the beginning of the game
def introduction(universe):
    help()
    look(universe)
