import random


class Condition:
    def __copy__(self, poison, hobbled, blind, immediate_damage):
        self.poison = poison
        self.hobbled = hobbled
        self.blind = blind
        self.immediate_damage = immediate_damage


poisoned = Condition()


class Weapon:
    def __init__(self, name, attack_bonus, damage, value, poisoned):
        self.name = name
        self.attack = attack_bonus
        self.damage = damage
        self.value = value
        self.poisoned = poisoned


unarmed = Weapon(name='fists', attack_bonus=0, damage=1, value=0, poisoned=False)
rusty_dagger = Weapon(name='rusty dagger', attack_bonus=0, damage=2, value=50, poisoned=False)
steel_sword = Weapon(name='steel sword', attack_bonus=1, damage=4, value=200, poisoned=False)
bow = Weapon(name='bow', attack_bonus=4, damage=3, value=300, poisoned=False)
poisoned_fangs = Weapon(name='poisoned fangs', attack_bonus=2, damage=1, value=0, poisoned=True)
god_weapon = Weapon(name='god_weapon', attack_bonus=20, damage=20, value=0, poisoned=False)

weapons = [unarmed, rusty_dagger, steel_sword, bow, poisoned_fangs, god_weapon]


class Enemy:
    def __init__(self, name, max_hp, hp, ac, attack, weapon, xp_worth):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.ac = ac
        self.attack = attack
        self.weapon = weapon
        self.xp_worth = xp_worth


goblin = Enemy(name="Goblin", max_hp=4, hp=4, ac=12, attack=4, weapon=rusty_dagger, xp_worth=1)
goblin_champion = Enemy(name="Goblin Champion", max_hp=6, hp=6, ac=14, attack=4, weapon=steel_sword, xp_worth=3)
kobold_archer = Enemy(name="Kobold Archer", max_hp=3, hp=3, ac=10, attack=6, weapon=bow, xp_worth=2)
spider = Enemy(name="Spider", max_hp=3, hp=3, ac=11, attack=5, weapon=poisoned_fangs, xp_worth=3)

enemy_types = [goblin, goblin_champion, kobold_archer, spider]


class PlayerCharacter:
    def __init__(self, max_hp, hp, ac, attack, weapon, xp, location):
        self.max_hp = max_hp
        self.hp = hp
        self.ac = ac
        self.attack = attack
        self.weapon = weapon
        self.xp = xp
        self.location = location


ranger = PlayerCharacter(max_hp=8, hp=8, ac=12, attack=2, weapon=bow, xp=0, location=0)
fighter = PlayerCharacter(max_hp=10, hp=10, ac=14, attack=4, weapon=steel_sword, xp=0, location=0)

player_classes = [ranger, fighter]


class Tile:
    def __init__(self, ways_out, trap_type, text_description, enemy, link0, link1, link2, link3, visited):
        self.ways_out = ways_out
        self.trap_type = trap_type
        self.text_description = text_description
        self.enemy = enemy
        self.link0 = link0  # link to back/previous tile
        self.link1 = link1  # link to next tile left if 1 or 3 ways out
        self.link2 = link2  # link to next tile forward if 1 or 3 ways out
        self.link3 = link3  # link to next tile right if 3 ways out
        self.visited = visited


cave_word1 = ['a dimly lit', 'an ominously dark', 'an eerily quiet',
              'an uncomfortably cold', 'a horribly humid']
cave_word2 = ['corridor', 'spot', 'room', 'cavern']
cave_word3 = ['with damp walls', 'with a slippery floor', 'traversed by a snaking creek']


def cave_description():
    descrip = random.choice(cave_word1) + " " + random.choice(cave_word2) + " " + random.choice(cave_word3) + "."
    return descrip
