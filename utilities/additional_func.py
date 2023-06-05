from random import randint


# Deletes mission from mission list when done.
def delete_mission(universe):
    reward = universe._cMission.reward()
    universe._cPlanet.erase_mission()
    print('_' * 45 + '\n')
    print(f"You have complited mission on planet {universe.get_player().location()}.\n")
    if reward > 0:
        print(f"Here is your reward: +{reward} gold.")
        universe.get_player().add_stat('gold', reward)
    print('_' * 45 + '\n')
    universe.get_current_Planet_Mission()


# Prints credits after finishing the game.
def show_credits(player):
    print('=' * 54 + '\n')
    print(f'Congratulations {player.get_name()}, you have finished your journey.')
    print('=' * 54 + '\n')
    print("Thank you for playing my game!  ~Jan Jędrzejewski\n")


# Prints information about figting with enemies
def duel(player, enemy):
    print(player.show_stats())
    print(enemy)
    if player.get_stat("power") <= enemy.armor():
        print("Your enemy has greater armor than your power!\n")
        return False
    if enemy.power() <= player.get_stat("armor"):
        print("You have overpowered your enemy.\n")
        return True
    player_pts = player.get_stat("health") / (enemy.power() - player.get_stat("armor"))
    enemy_pts = enemy.health() / (player.get_stat("power") - enemy.armor())
    print(f"\nYour combat points: {player_pts:.3f}".ljust(25) + f" Enemy combat points: {enemy_pts:.3f}\n")
    if player_pts > enemy_pts:
        print(f"You have won the battle with {enemy.get_name()}!\n")
        reward = enemy.reward()
        if reward > 0:
            player.add_stat('gold', reward)
            print(f"Here is your reward +{reward} gold!\n")
        return True
    return None


# Alternative way of fighting with enemies
def duel2(player, enemy):
    print(player.show_stats())
    print(enemy)
    enemy_dmg = player.get_stat("power") - enemy.armor()
    if enemy_dmg < 0:
        enemy_dmg = 0
    player_dmg = enemy.power() - player.get_stat("armor")
    if player_dmg < 0:
        player_dmg = 0
    player.take_damage(player_dmg)
    enemy.take_damage(enemy_dmg)
    print(f"\nYou attacked {enemy.get_name()} -{enemy_dmg} health")
    print(f"{enemy.get_name()} attacked you back -{player_dmg} health\n")
    if player.get_stat("health") <= 0:
        player.add_stat("health", player_dmg)
        print("Hou died in a heroic fight. Heroes will be remembered forever!")
        show_credits(player)
        exit()
    if enemy.is_dead():
        print("You have killed your enemy.")
        reward = enemy.reward()
        if reward > 0:
            player.add_stat('gold', reward)
            print(f"Here is your reward +{reward} gold!\n")
        return True
    return False


# Generates sentences for look_command.
def generate_sentence(name, itemType):
    positions = [
        "lying", "standing", "sitting", "situated", "placed", "settled", "set",
        "located", "positioned"
    ]
    wheres = [
        "near", "next to", "aside", "nearby", "close to",
        "in close proximity to", "side-by-side", "alongside"
    ]
    objects = [
        "a bush swaying in the wind", "a lively fountain", "a hot lava stream",
        "an enormous owk tree", "a funny looking rock formation",
        "a deep and dark crater", "a shapeshifting, red alien with family"
    ]
    starts = [
        "There's", "There is", "You can see", "You see", "You notice",
        "You catch a glimpse of", "You are able to detect",
        "You are able to glimpse", "You spot"
    ]

    start = starts[randint(0, len(starts) - 1)]
    position = positions[randint(0, len(positions) - 1)]
    where = wheres[randint(0, len(wheres) - 1)]
    obj = objects[randint(0, len(objects) - 1)]

    text = ''

    if itemType == "npc":
        text = start + f" '{name}', " + position + ' ' + where + ' ' + obj + '.\n'
    elif itemType == "enemy":
        text = start + f" an angry looking '{name}' " + position + ' ' + where + ' ' + obj + '.\n'
    elif itemType == "item":
        text = start + f" a '{name}' " + position + ' ' + where + ' ' + obj + '.\n'
    elif itemType == "store":
        text = f"There is a {name} on this planet."
    return text
