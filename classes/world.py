from classes.planet import Planet
from classes.mission import Mission
from classes.player import Player
import json
from utilities.file_data import SAVE
from utilities.errors import WrongPlayerError
from utilities.errors import WrongMapInFileError
from utilities.errors import NoPlanetsError
from utilities.errors import NoMissionsError
from utilities.errors import WrongPlanetError
from utilities.errors import WrongMissionError

'''
World class organises the whole universe of the game (missions, planets, etc).
'''


class World:
    def __init__(self, file):
        try:
            self._player = Player(file)
        except Exception:
            raise WrongPlayerError
        try:
            self._map = Map(file)
        except Exception:
            WrongMapInFileError
        self._planets = self._load_planets(file)
        self._missions = self._load_missions(file)

    # Creates dict of Mission objects from the file.
    def _load_missions(self, file):
        missionDict = dict()
        for mission in self._map._missionList:
            if mission in file["missions"]:
                missionDict[mission] = Mission(file["missions"][f"{mission}"], file)
            else:
                raise WrongMissionError(mission)
        return missionDict

    # Creates dict of Planet objects from the file.
    def _load_planets(self, file):
        planetDict = dict()
        for planet in self._map._planetList:
            if planet in file["planets"]:
                planetDict[planet] = Planet(file["planets"][f"{planet}"], file)
            else:
                WrongPlanetError(planet)
        return planetDict

    # Returns mission object for given location.
    def get_mission_for_location(self, location):
        missionId = self._planets[location].get_mission()
        if missionId:
            return self._missions[missionId]
        else:
            return None

    # Returns planet object for given location.
    def get_planet_for_location(self, location):
        return self._planets[location]

    # Returns player object.
    def get_player(self):
        return self._player

    # Returns Planet object and Mission object for current location of player.
    def get_current_Planet_Mission(self):
        self._cPlanet = self._planets[self._player.location()]
        self._cMission = self.get_mission_for_location(self._player.location())
        return self._cPlanet, self._cMission

    # Saves current status of the world into the SAVE file.
    def save(self):
        self._player.save(SAVE)

        with open(SAVE) as f:
            savedFile = json.load(f)

        for planet in self._map._planetList:
            savedFile["planets"][planet]["missions"] = self._planets[planet].get_missions()
        for mission in self._map._missionList:
            savedFile["missions"][mission] = self._missions[mission].to_json(savedFile)

        with open(SAVE, 'w') as f:
            json.dump(savedFile, f)

    # Checks if all missions in the game have been complited.
    def end_of_game(self):
        for planet in self._planets:
            if self._planets[planet].get_mission():
                return False
        return True


'''
Map class organises the map layout,
and finds available paths from each location.
'''


class Map:
    def __init__(self, file):
        self._map = file["map"]["locations"]
        self._paths = self._find_paths()
        self._planetList, self._missionList = self._get_data(file)
        if self._planetList == []:
            raise NoPlanetsError
        if self._missionList == []:
            raise NoMissionsError

    # Returns lists of planets names and missions id in existing map.
    def _get_data(self, file):
        planets = []
        missions = []
        for row in self._map:
            for planet in row:
                if len(planet) > 1:
                    planets.append(planet)
                    for mission in file["planets"][f"{planet}"]["missions"]:
                        missions.append(mission)
        return planets, missions

    # Returns all available paths to other planets for a given location.
    def available_paths(self, location):
        return self._paths[f"{location}"]

    # Returns a dictionary of all possible paths for each planet.
    def _find_paths(self):
        neighbors = dict()
        i = 1
        while i < len(self._map) - 1:
            j = 1
            while j < len(self._map[i]) - 1:
                if self._map[i][j] != "":
                    all_neighbors = [
                        self._map[i - 1][j],      # top neighbor
                        self._map[i - 1][j - 1],  # top right
                        self._map[i - 1][j + 1],  # top left
                        self._map[i][j + 1],      # right neighbor
                        self._map[i][j - 1],      # left neighbor
                        self._map[i + 1][j],      # bottom neighbor
                        self._map[i + 1][j - 1],  # bottom right
                        self._map[i + 1][j + 1]]   # bottom left

                    new = []
                    for item in all_neighbors:
                        if len(item) > 1:
                            new.append(item)
                    neighbors[self._map[i][j]] = new
                j += 1
            i += 1

        return neighbors
