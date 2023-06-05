from classes.world import World, Map, Mission
from classes.planet import Planet, Store
from classes.character import Npc

File = {
    "player": {
        "name": "Frank",
        "health": 100,
        "power": 20,
        "armor": 30,
        "fuel": 150,
        "gold": 200,
        "location": "Earth",
        "items": []
    },
    "map": {
        "locations": [
            ["",        "",      "",    ""],
            ["", "Mercury",      "",    ""],
            ["",        "",  "Earth",   ""],
            ["",        "",      "",    ""]
        ]
    },
    "planets": {
        "Mercury": {
            "visited": 0,
            "description": "With conditions as extreme as these, the chances of sustaining life on this planet are virtually none-existent.",
            "missions": [],
            "stores": []
        },
        "Earth": {
            "visited": 0,
            "description": "From heart of fire to white capped peaks, Earth is mother and home.",
            "missions": ["Earth1"],
            "stores": ["earth_store"]
        }
    },
    "missions":
    {
        "Earth1": {
            "description": "You have landed successfully on planet Earth, with last galons of fuel",
            "surroundings": "",
            "items": ["Beer"],
            "npc": ["Eth0"],
            "enemies": [],
            "reward": 20,
            "help": "Talk to William",
            "required": ["Bomb"]
        },
    },
    "characters": {
        "Eth0": {
            "id": "Eth0",
            "name": "William",
            "type": "friendly",
            "dialog": ["Welcome Adventurer! \n We're glad, you've decided to join our bounty hunting guild. \n I hope we will make tons of money together. \n Go talk to Elijah. He has a first job for you. \n I think You'll find him in Titanus Colony on Mars"],
            "items": []
        }
    },
    "stores": {
        "earth_store": {
            "name": "Local Shop",
            "description": "This is the first shop in the universe.",
            "items": ["Bomb", "Beer", "small_gas_tank", "Small_pistol"]

        },
        "mars_store": {
            "name": "Mars gas station",
            "description": "Cheapest gas in solar system!",
            "items": ["Bomb", "Beer"]

        }
    },
    "items": {
        "small_gas_tank": {
            "id": "small_gas_tank",
            "name": "Small Fuel Tank",
            "price": 15,
            "fuel": 30
        },
        "Beer": {
            "id": "Beer",
            "name": "Pint of galactic beer",
            "price": 50,
            "health": 100
        },
        "Bomb": {
            "id": "Bomb",
            "name": "Astral Barrel Bomb",
            "price": 15,
            "power": 15
        },
        "Small_pistol": {
            "inventory": True,
            "id": "Small_pistol",
            "name": "Small Pistol",
            "power": 15
        }
    }
}


def test_World_init():
    world = World(File)
    assert type(world._map) == Map
    assert type(world._planets["Earth"]) == Planet
    assert type(world._missions["Earth1"]) == Mission
    assert type(world._planets["Earth"]._store) == Store


def test_Map_init():
    maps = Map(File)
    assert maps._paths["Earth"] == ["Mercury"]
    assert maps._paths["Mercury"] == ["Earth"]
    assert "Mercury" in maps._planetList
    assert "Earth1" in maps._missionList


def test_Planet_init():
    planet = Planet(File["planets"]["Earth"], File)
    assert planet._description == "From heart of fire to white capped peaks, Earth is mother and home."
    assert "Earth1" in planet._missions
    assert type(planet._store) == Store
    assert planet._store.get_name() == "Local Shop"


def test_Planet_methods():
    planet = Planet(File["planets"]["Earth"], File)
    assert planet.get_mission() == "Earth1"
    planet.erase_mission()
    assert planet.get_missions() == []
    assert planet.if_store_on_planet() is True
    assert type(planet.get_store()) == Store


def test_Mission_init():
    mission = Mission(File["missions"]["Earth1"], File)
    assert mission._description == "You have landed successfully on planet Earth, with last galons of fuel"
    assert mission._reward == 20
    assert mission._items[0].get_name() == "Pint of galactic beer"
    assert mission._npcs[0].get_name() == "William"
    assert mission._enemies == []
    assert mission._required[0].get_name() == "Astral Barrel Bomb"


def test_Missions_names_lists():
    mission = Mission(File["missions"]["Earth1"], File)
    assert mission.get_items() == ["Pint of galactic beer"]
    assert mission.get_npcs() == ["William"]
    assert mission.get_enemies() == []
    assert mission.get_required() == ["Astral Barrel Bomb"]


def test_Missions_get_objects_delete():
    mission = Mission(File["missions"]["Earth1"], File)
    npc = mission.get_npc_obj("William")
    assert type(npc) == Npc
    mission.delete_npc(npc.get_id())
    assert mission.get_npcs() == []
    assert mission.get_required() == ["Astral Barrel Bomb"]
    mission.delete_required("Bomb")
    assert mission.get_required() == []


def test_Missions_methods():
    mission = Mission(File["missions"]["Earth1"], File)
    npc = mission.get_npc_obj("William")
    assert mission.__str__() == "You have landed successfully on planet Earth, with last galons of fuel"
    assert mission.check_if_done() is False
    assert mission.reward() == 20
    mission.delete_npc(npc.get_id())
    mission.delete_required("Bomb")
    mission.take_item("Pint of galactic beer")
    assert mission.check_if_done() is True


def test_Store_init():
    store = Store(File["stores"]["earth_store"], File)
    assert store.get_name() == "Local Shop"
    assert store._description == "This is the first shop in the universe."
    assert store._items_id == ["Bomb", "Beer", "small_gas_tank", "Small_pistol"]


def test_Store_printing():
    store = Store(File["stores"]["mars_store"], File)
    assert store._description == "Cheapest gas in solar system!"
    assert store.get_name() == "Mars gas station"
    description = "1. Astral Barrel Bomb         Cost: 15 gold\n"
    description += "\t~ power: +15\n"
    description += "2. Pint of galactic beer      Cost: 50 gold\n"
    description += "\t~ health: +100\n"
    assert store.show_items() == description
