from classes.item import Item
from classes.character import Npc, Enemy
from utilities.additional_func import generate_sentence

'''
Mission class provides support for doing tasks, etc.
'''


class Mission:
    def __init__(self, mission, file):
        self._description = mission["description"]
        self._reward = mission["reward"]
        self._help = mission["help"]
        self._items = self._from_json_items(mission, file)
        self._npcs = self._from_json_npc(mission, file)
        self._enemies = self._from_json_enemies(mission, file)
        self._required = self._from_json_required(mission, file)
        self._around = self._generate_surroundings()

    def __str__(self):
        return self._description

    def hint(self):
        return self._help

    def reward(self):
        return self._reward

    # Returns true when all list of things to do are empty
    def check_if_done(self):
        if len(self._items) == 0 and len(self._npcs) == 0 and len(self._enemies) == 0 and len(self._required) == 0:
            return True
        return False

    # Returns list of names
    def get_items(self):
        return [item.get_name() for item in self._items]

    def get_npcs(self):
        return [person.get_name() for person in self._npcs]

    def get_enemies(self):
        return [enemy.get_name() for enemy in self._enemies]

    def get_required(self):
        return [item.get_name() for item in self._required]

    # Returns type object for given id
    def get_npc_obj(self, name):
        for npc in self._npcs:
            if npc.get_name() == name:
                return npc
        return None

    def get_enemy_obj(self, name):
        for enemy in self._enemies:
            if enemy.get_name() == name:
                return enemy
        return None

    # Delete type object for given id
    def delete_npc(self, id):
        for npc in self._npcs:
            if npc.get_id() == id:
                self._npcs.remove(npc)

    def delete_enemy(self, id):
        for enemy in self._enemies:
            if enemy.get_id() == id:
                self._enemies.remove(enemy)

    def delete_required(self, id):
        for item in self._required:
            if item.get_id() == id:
                self._required.remove(item)

    # Returns item and delete item from mission list by given id
    # returns None if id does not match any items
    def take_item(self, name):
        for item in self._items:
            if item.get_name() == name:
                self._items.remove(item)
                return item
        for item in self._required:
            if item.get_name() == name:
                self._required.remove(item)
                return item
        return None

    # Creates object lists
    def _from_json_items(self, mission, file):
        return [Item(file["items"][itemName]) for itemName in mission["items"]]

    def _from_json_npc(self, mission, file):
        return [Npc(file["characters"][npcName]) for npcName in mission["npc"]]

    def _from_json_enemies(self, mission, file):
        return [Enemy(file["characters"][enemyName]) for enemyName in mission["enemies"]]

    def _from_json_required(self, mission, file):
        return [Item(file["items"][requiredName]) for requiredName in mission["required"]]

    # Prepers dict from mission data to save
    def to_json(self, file):
        missionData = {
            "description": self._description,
            "items": self._items_list(),
            "npc": self._npcs_list(),
            "enemies": self._enemies_list(),
            "required": self._required_list(),
            "reward": self._reward,
            "help": self._help
        }
        return missionData

    # Returns list of ids
    def _items_list(self):
        return [item.get_id() for item in self._items]

    def _npcs_list(self):
        return [npc.get_id() for npc in self._npcs]

    def _enemies_list(self):
        return [enemy.get_id() for enemy in self._enemies]

    def _required_list(self):
        return [item.get_id() for item in self._required]

    # Return surroundings on planet based an current mission.
    def get_surroundings(self):
        self._around = self._generate_surroundings()
        return self._around

    # Generates hints for mission
    def _generate_surroundings(self):
        if self.check_if_done():
            return None
        hints = ''
        for item in self._items:
            name = item.get_name()
            hints += generate_sentence(name, "item")
        for npc in self._npcs:
            name = npc.get_name()
            hints += generate_sentence(name, "npc")
        for enemy in self._enemies:
            name = enemy.get_name()
            hints += generate_sentence(name, "enemy")
        for item in self._required:
            name = item.get_name()
            hints += generate_sentence(name, "required")
        return hints
