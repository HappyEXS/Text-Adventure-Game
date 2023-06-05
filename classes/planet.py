from classes.item import Item

'''
Planet class provides basic informations about planet.
'''


class Planet:
    def __init__(self, planetData, file):
        self._description = planetData["description"]
        self._missions = planetData["missions"]
        self._store = self._get_store(planetData["stores"], file)

    def __str__(self):
        return self._description

    # Creates Store object from list of stores
    def _get_store(self, stores, file):
        if stores:
            store = stores[0]
            return Store(file["stores"][f"{store}"], file)
        else:
            return None

    # Returns a Store object for the planet (or None).
    def get_store(self):
        return self._store

    # Checks if there is a store on this planet.
    def if_store_on_planet(self):
        if self._store:
            return True
        return False

    # Returns current mission id on the planet.
    def get_mission(self):
        if self._missions:
            return self._missions[0]
        else:
            return None

    # Returns all missions ids on the planet.
    def get_missions(self):
        return self._missions

    # Erases finished mission.
    def erase_mission(self):
        self._missions.pop(0)


'''
Store class provides support for shop in the game.
'''


class Store():
    def __init__(self, storeData, file):
        self._name = storeData["name"]
        self._description = storeData["description"]
        self._items_id = storeData["items"]
        self._items = self._get_items(file)

    # Creates list of item objets in shop.
    def _get_items(self, file):
        items = []
        for item in self._items_id:
            items.append(Item(file["items"][item]))
        return items

    # Returns shop's name.
    def get_name(self):
        return self._name

    def get_item(self, number):
        return self._items[number]

    # Returns list of items names.
    def get_items_ids(self):
        return self._items_id

    # Returns informations about shop and items that can be bought.
    def __str__(self):
        description = '_' * 45 + '\n'
        description += self._description + "\n"
        description += self.show_items()
        description += '_' * 45
        return description

    # Returns string of all items and their cost and stats in shop.
    def show_items(self):
        i = 1
        text = ""
        for item in self._items:
            text += f'{i}. ' + item.__str__()
            i += 1
        return text
