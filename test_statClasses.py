from classes.stats import Stats
from classes.item import Item
from classes.character import Npc, Enemy, Character
from classes.player import Player

File = {
    "player": {
        "name": "Frank",
        "health": 100,
        "power": 20,
        "armor": 30,
        "fuel": 150,
        "gold": 200,
        "location": "Earth",
        "items": ["Sack_of_gold", "Bomb"]
    },
    "items": {
        "Sack_of_gold": {
            "id": "Sack_of_gold",
            "name": "Sack of gold",
            "gold": 200,
            "fuel": 200
        },
        "Bomb": {
            "id": "Bomb",
            "name": "Astral Barrel Bomb",
            "price": 15,
            "power": 15
        },
        "Teleprop": {
            "inventory": True,
            "id": "Teleprop",
            "name": "Teleprop",
            "price": 0,
            "power": 15
        },
        "medium_gas_tank": {
            "id": "medium_gas_tank",
            "name": "Medium Fuel Tank",
            "price": 30,
            "fuel": 60
        }
    },
    "characters": {
        "Eth0": {
            "id": "Eth0",
            "name": "William",
            "dialog": ["""Welcome Adventurer!\n
            We're glad, you've decided to join our bounty hunting guild."""],
            "items": []
        },
        "Sat1": {
            "id": "Sat1",
            "name": "Spaceball One with Dark Helmet on board",
            "reward": 100,
            "health": 100,
            "power": 120,
            "armor": 50,
        }
    }
}


def test_Stats_init():
    statistics = Stats('Bob', 30, 5, 10, 100, 200)
    assert statistics.get_name() == 'Bob'
    assert statistics._health == 30
    assert statistics._power == 5
    assert statistics._armor == 10
    assert statistics._fuel == 100
    assert statistics._gold == 200


def test_Stats_add_stat():
    statistics = Stats('Bob', 30, 5, 10, 100, 200)
    assert statistics.get_name() == 'Bob'
    statistics.add_stat('health', 10)
    assert statistics._health == 40
    statistics.add_stat('power', 10)
    assert statistics._power == 15
    statistics.add_stat('armor', 5)
    assert statistics._armor == 15
    statistics.add_stat('fuel', -50)
    assert statistics._fuel == 50
    statistics.add_stat('gold', -30)
    assert statistics._gold == 170


def test_Stats_get_stat():
    statistics = Stats('Bob', 30, 5, 10, 100, 200)
    assert statistics.get_name() == 'Bob'
    assert statistics.get_stat('health') == 30
    assert statistics.get_stat('power') == 5
    assert statistics.get_stat('armor') == 10
    assert statistics.get_stat('fuel') == 100
    assert statistics.get_stat('gold') == 200


def test_Player_init():
    player = Player(File)
    assert player.get_name() == "Frank"
    assert player._health == 100
    assert player._power == 20
    assert player._armor == 30
    assert player._fuel == 150
    assert player._gold == 200
    assert player._location == "Earth"


def test_Player_items():
    player = Player(File)
    sack = Item(File["items"]["Sack_of_gold"])
    barrel = Item(File["items"]["Bomb"])
    assert "Sack_of_gold", "Bomb" in player._itemsNames
    assert barrel, sack in player._items


def test_Player_location():
    player = Player(File)
    assert player.location() == "Earth"
    assert player._fuel == 150
    player.set_location("Mars")
    player.add_stat("fuel", -20)
    assert player.location() == "Mars"
    assert player._fuel == 130


def test_Player_not_enought_fuel():
    player = Player(File)
    player.add_stat('fuel', -145)
    assert player._fuel == 5
    # player.use_fuel(10)


def test_Player_pickup_item():
    player = Player(File)
    item = Item(File["items"]["Teleprop"])
    player.pickup_item(item)
    assert item in player._items
    assert player._power == 35


def test_Player_buy_item():
    player = Player(File)
    item = Item(File["items"]["medium_gas_tank"])
    player.buy_item(item)
    assert item not in player._items
    assert player._fuel == 210
    assert player._gold == 170


def test_Character_init():
    character = Character(File["characters"]["Eth0"])
    assert character.get_name() == "William"


def test_Enemy_init():
    character = Enemy(File["characters"]["Sat1"])
    assert character.get_name() == "Spaceball One with Dark Helmet on board"
    assert character.reward() == 100


def test_Npc_init():
    character = Npc(File["characters"]["Eth0"])
    assert character.get_name() == "William"
    assert character.get_dialog() == """Welcome Adventurer!\n
            We're glad, you've decided to join our bounty hunting guild."""


def test_Item_init():
    item = Item(File["items"]["medium_gas_tank"])
    assert item.get_name() == "Medium Fuel Tank"
    assert item.get_id() == "medium_gas_tank"
    assert item.get_price() == 30
    assert item.get_inventory() is False
    assert item.get_stat('health') == 0
    assert item.get_stat('fuel') == 60
