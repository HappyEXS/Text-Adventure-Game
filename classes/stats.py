from utilities.errors import WrongTypeStatsError
from utilities.errors import NegativeStatsError

'''
Stats calss provides basic actions for statistics existing in game,
such as saving values, updating them and returning.
'''


class Stats():
    def __init__(self, name, health, power, armor, fuel, gold):
        self._name = str(name)
        try:
            self._health = int(health)
            self._power = int(power)
            self._armor = int(armor)
            self._fuel = int(fuel)
            self._gold = int(gold)
        except ValueError:
            raise WrongTypeStatsError(self._name)
        if self._power < 0 or self._armor < 0 or self._fuel < 0 or self._gold < 0 or self._health < 0:
            raise NegativeStatsError(self._name)

    def get_name(self):
        return self._name

    # Adds given value(int) for given stat(str)
    def add_stat(self, stat, value):
        if stat == 'health':
            self._health += value
        if stat == 'power':
            self._power += value
        if stat == 'armor':
            self._armor += value
        if stat == 'fuel':
            self._fuel += value
        if stat == 'gold':
            self._gold += value

    # Returns value of give stat(str)
    def get_stat(self, stat):
        if stat == 'health':
            return self._health
        if stat == 'power':
            return self._power
        if stat == 'armor':
            return self._armor
        if stat == 'fuel':
            return self._fuel
        if stat == 'gold':
            return self._gold
