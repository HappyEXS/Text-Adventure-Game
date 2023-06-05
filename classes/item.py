from classes.stats import Stats
from utilities.errors import WrongItemError

'''
Item class based on Stats
Contains objects that player can posses and keep in the inventory.
'''


class Item(Stats):
    def __init__(self, itemData):
        try:
            name = itemData["name"]
            self._id = itemData["id"]
            if "price" in itemData:
                self._price = itemData["price"]
            else:
                self._price = None
            if "inventory" in itemData:
                self._inventory = itemData["inventory"]
            else:
                self._inventory = False
            # Following loop creates list of tuples (self._stats) where
            # firs argument is name of stat and second is value that this item gives
            # Also creates list of statistics in order (statistics) for super.()__init__
            stats = ['health', 'power', 'armor', 'fuel', 'gold']
            statistics = []
            self._stats = []
            for stat in stats:
                if stat in itemData:
                    statistics.append(itemData[stat])
                    self._stats.append((stat, itemData[stat]))
                else:
                    statistics.append(0)
            super().__init__(name, statistics[0], statistics[1], statistics[2], statistics[3], statistics[4])
        except ValueError:
            raise WrongItemError

    # Returns formatted informations about item
    def __str__(self):
        description = f"{self.get_name()}".ljust(27)
        if self.get_price() is None or self.get_price() == 0:
            description += '\n'
        else:
            description += f'Cost: {self.get_price()} gold\n'
        for stat in self.get_stats():
            description += f"\t~ {stat[0]}: +{stat[1]}\n"
        return description

    def get_id(self):
        return self._id

    def get_price(self):
        return self._price

    def get_inventory(self):
        return self._inventory

    def get_stats(self):
        return self._stats
