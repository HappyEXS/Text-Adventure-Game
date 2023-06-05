class WrongTypeStatsError(Exception):
    def __init__(self, name):
        super().__init__(f"Stats cannot be negative!\nObject name:{name}")


class NotPositiveHealthError(Exception):
    def __init__(self, name, health):
        super().__init__(f"Health must be positive!\nPlayer name: '{name}'' Health value: {health}")


class NegativeStatsError(Exception):
    def __init__(self, name):
        super().__init__(f"Stats cannot be negative!\nObject name:{name}")


class WrongMapInFileError(Exception):
    def __init__(self):
        super().__init__("There is no 'map' in file")


class NoPlanetsError(Exception):
    def __init__(self):
        super().__init__("There are 0 planets in map. Nuber of planets must be positive.")


class NoMissionsError(Exception):
    def __init__(self):
        super().__init__("There are 0 missions on planets in map. Nuber of missions must be positive.")


class WrongPlanetError(Exception):
    def __init__(self, name):
        super().__init__(f"Check planet: {name} in file.")


class WrongMissionError(Exception):
    def __init__(self, name):
        super().__init__(f"Check mission: {name} in file.")


class WrongItemError(Exception):
    def __init__(self):
        super().__init__("Check items in file.")


class WrongCharacterError(Exception):
    def __init__(self):
        super().__init__("Check characters in file.")


class WrongPlayerError(Exception):
    def __init__(self):
        super().__init__("Check player in file.")
