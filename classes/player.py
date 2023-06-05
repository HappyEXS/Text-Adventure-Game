import json
from classes.stats import Stats
from classes.item import Item
from utilities.errors import NotPositiveHealthError

'''
Player class performs actions for player.
'''


class Player(Stats):
    def __init__(self, file):
        name = file["player"]["name"]
        health = file["player"]["health"]
        power = file["player"]["power"]
        armor = file["player"]["armor"]
        fuel = file["player"]["fuel"]
        gold = file["player"]["gold"]
        self._location = file["player"]["location"]
        super().__init__(name, health, power, armor, fuel, gold)
        if self._health <= 0:
            raise NotPositiveHealthError(self._name, self._health)

        self._items = self._load_items(file)
        self._itemsNames = self._load_items_names()

    def __str__(self):
        description = f'{self._name}, you have {self._health} points of health.\n'
        description += f"Your current power is {self._power} and your armor {self._armor}.\n"
        description += f"You have {self._gold} gold. Your ship has {self._fuel} galons of fuel.\n"
        description += self.show_items()
        return description

    # Returns formated statistics of player
    def show_stats(self):
        description = f"Your stats:\t Fuel: {self._fuel}\t Gold: {self._gold}\n"
        description += f" Health: {self._health}\t Power: {self._power}\t Armor: {self._armor}\n"
        return description

    # Returns current location - planet name that player is on
    def location(self):
        return self._location

    # Sets location for new planet name
    def set_location(self, newLocation):
        self._location = newLocation

    # Reduces healt ponts by given damage
    def take_damage(self, health):
        self._health -= health

    # Returns list of item objects for items in the inventory
    def get_items(self):
        return self._items

    # Saves current player information to file path
    def save(self, path):
        playerStats = {
            "name": self._name,
            "health": self._health,
            "power": self._power,
            "armor": self._armor,
            "fuel": self._fuel,
            "gold": self._gold,
            "location": self._location,
            "items": self._load_items_ids()
        }

        with open(path) as f:
            savedFile = json.load(f)

        savedFile["player"] = playerStats

        with open(path, 'w') as f:
            json.dump(savedFile, f)

    # Returns formated information about items in the inventory.
    def show_items(self):
        description = ""
        if self._itemsNames:
            if len(self._itemsNames) == 1:
                description = (f'You have a {self._itemsNames[0]} in the inventory.')
            elif len(self._itemsNames) == 2:
                description = (f'You have a {self._itemsNames[0]} and a {self._itemsNames[1]} in the inventory.')
            else:
                description = 'In the inventory you are carrying following items:\n'
                for name in self._itemsNames[:-1]:
                    description += f"{name}, "
                description += f'and {self._itemsNames[-1]}.'
        else:
            description = "Your inventory is empty."
        return description

    # Loads list of item objecs from file
    def _load_items(self, file):
        itemsObject = []
        for item in file["player"]["items"]:
            itemsObject.append(Item(file["items"][item]))
        return itemsObject

    # Loads list of item's names in inventoryt from item objects
    def _load_items_names(self):
        itemNames = []
        for item in self._items:
            itemNames.append(item.get_name())
        return itemNames

    # Loads list of item's ids in inventory
    def _load_items_ids(self):
        itemIds = []
        for item in self._items:
            itemIds.append(item.get_id())
        return itemIds

    # Performs buying item, pick ups item and pays for it
    def buy_item(self, item):
        self.add_stat("gold", -item.get_price())
        self.pickup_item(item)

    # Adds given item to infentory and updates player stats
    def pickup_item(self, item):
        for stat in item.get_stats():
            self.add_stat(stat[0], stat[1])
        if item.get_inventory():
            self._items.append(item)
            self._itemsNames.append(item.get_name())
