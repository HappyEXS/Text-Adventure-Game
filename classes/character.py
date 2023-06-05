from utilities.errors import WrongTypeStatsError
from utilities.errors import NegativeStatsError
from utilities.errors import NotPositiveHealthError
from utilities.errors import WrongCharacterError

'''
Basic class for characters
'''


class Character():
    def __init__(self, data):
        try:
            self._name = data["name"]
            self._id = data["id"]
        except ValueError:
            raise WrongCharacterError

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id


'''
Hostile characters that player can fight with.
'''


class Enemy(Character):
    def __init__(self, enemyData):
        super().__init__(enemyData)
        try:
            self._reward = enemyData["reward"]
            self._health = enemyData["health"]
            self._power = enemyData["power"]
            self._armor = enemyData["armor"]
        except ValueError:
            raise WrongTypeStatsError(self._name)
        if self._health <= 0:
            raise NotPositiveHealthError(self._name, self._health)
        if self._power < 0 or self._armor < 0:
            raise NegativeStatsError(self._name)

    def __str__(self):
        description = f"[{self._name}]\nHealth: {self._health}\tPower: {self._power}\tArmor: {self._armor}"
        return description

    def power(self):
        return self._power

    def health(self):
        return self._health

    def armor(self):
        return self._armor

    def reward(self):
        return self._reward

    # Reduces enemy's health by given amount
    def take_damage(self, health):
        self._health -= health

    # Returns true when enemy's hp is equal or below zero
    def is_dead(self):
        if self._health <= 0:
            return True
        return False


'''
Friendly characters that player can talk to.
'''


class Npc(Character):
    def __init__(self, npcData):
        super().__init__(npcData)
        self._dialog = npcData["dialog"]

    def __str__(self):
        return f"[{self._name}]\n{self._dialog[0]}\n"

    def get_dialog(self):
        return self._dialog[0]
