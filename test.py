import sys
import math


def log(*x):
    print(*x, file=sys.stderr)

def distance(a, b):
    return math.dist(a, b) 


class Entities:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Spawn(Entities):
    def __init__(self, x, y, entityType, radius):
        super().__init__(x, y)
        self.entityType = entityType
        self.radius = radius


class Units:
    def __init__(self, _id, unitType, x , y, attackRange, health, max_health, shield, attack_damage, movement_speed, stun, gold):
        self._id = _id
        self.unitType = unitType
        self.x, self.y = x, y
        self.attackRange = attackRange
        self.health = health
        self.max_health = max_health
        self.shield = shield
        self.attack_damage = attack_damage
        self.movement_speed = movement_speed
        self.stun = stun
        self.gold = gold


class Heros(Units):
    def __init__(self, _id, unitType, x, y, attackRange, health, max_health, shield, attack_damage, movement_speed, stun, gold, countDown1, countDown2, countDown3, mana, maxMana, manaRegen, hero, isVisible, items):
        super().__init__(_id, unitType, x, y, attackRange, health, max_health, shield, attack_damage, movement_speed, stun, gold)
        self.countDown1 = countDown1
        self.countDown2 = countDown2
        self.countDown3 = countDown3
        self.mana = mana
        self.maxMana = maxMana
        self.manaRegen = manaRegen
        self.hero = hero
        self.isVisible = isVisible
        self.items = items


class Items:
    def __init__(self, name, cost, damage, health, maxHealth, mana, maxMana, speed, manaRegen, isPotion):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.health = health
        self.maxHealth = maxHealth
        self.mana = mana
        self.maxMana = maxMana
        self.speed = speed
        self.manaRegen = manaRegen
        self.isPotion = isPotion

    def __repr__(self):
        return f"{self.name}: {self.cost}"


Hero = "HULK"
spawnPoints = []
items = []
my_team = int(input())
# useful from wood1, represents the number of bushes and the number of places where neutral units can spawn
bush_and_spawn_point_count = int(input())
for i in range(bush_and_spawn_point_count):
    inputs = input().split()
    entity_type = inputs[0]  # BUSH, from wood1 it can also be SPAWN
    x = int(inputs[1])
    y = int(inputs[2])
    radius = int(inputs[3])
    spawnPoints.append(Spawn(x, y, entity_type, radius))

item_count = int(input())  # useful from wood2
for i in range(item_count):
    inputs = input().split()
    log(inputs)
    # contains keywords such as BRONZE, SILVER and BLADE, BOOTS connected by "_" to help you sort easier
    item_name = inputs[0]
    # BRONZE items have lowest cost, the most expensive items are LEGENDARY
    item_cost = int(inputs[1])
    # keyword BLADE is present if the most important item stat is damage
    damage = int(inputs[2])
    health = int(inputs[3])
    max_health = int(inputs[4])
    mana = int(inputs[5])
    max_mana = int(inputs[6])
    # keyword BOOTS is present if the most important item stat is moveSpeed
    move_speed = int(inputs[7])
    mana_regeneration = int(inputs[8])
    is_potion = int(inputs[9])  # 0 if it's not instantly consumed
    items.append(Items(item_name, item_cost, damage, health, max_health,
                 mana, max_mana, move_speed, mana_regeneration, is_potion))

potion = ""
weapons = []
for item in items:
    if "Blade" in item.name:
        weapons.append(item)
weapons = sorted(weapons, key=lambda x: x.cost)
log(weapons)


# game loop
while True:
    myUnits = []
    myHeros = []
    oppUnits = []
    oppHeros = []
    gold = int(input())
    enemy_gold = int(input())
    # a positive value will show the number of heroes that await a command
    round_type = int(input())
    
    entity_count = int(input())
    for i in range(entity_count):
        inputs = input().split()
        # log(inputs)
        unit_id = int(inputs[0])
        team = int(inputs[1])
        # UNIT, HERO, TOWER, can also be GROOT from wood1
        unit_type = inputs[2]
        x = int(inputs[3])
        y = int(inputs[4])
        attack_range = int(inputs[5])
        health = int(inputs[6])
        max_health = int(inputs[7])
        shield = int(inputs[8])  # useful in bronze
        attack_damage = int(inputs[9])
        movement_speed = int(inputs[10])
        stun_duration = int(inputs[11])  # useful in bronze
        gold_value = int(inputs[12])
        # all countDown and mana variables are useful starting in bronze
        count_down_1 = int(inputs[13])
        count_down_2 = int(inputs[14])
        count_down_3 = int(inputs[15])
        mana = int(inputs[16])
        max_mana = int(inputs[17])
        mana_regeneration = int(inputs[18])
        # DEADPOOL, VALKYRIE, DOCTOR_STRANGE, HULK, IRONMAN
        hero_type = inputs[19]
        is_visible = int(inputs[20])  # 0 if it isn't
        items_owned = int(inputs[21])  # useful from wood1
        unit = Units(unit_id, unit_type, x, y, attack_range, health, max_health, shield, attack_damage, movement_speed, stun_duration, gold_value)
        if team == my_team:
            if unit_type == "HERO":
                myHeros.append(Heros(unit_id, unit_type, x, y, attack_range, health, max_health, shield, attack_damage, movement_speed, stun_duration,
                                  gold_value,count_down_1, count_down_2, count_down_3, mana, max_mana, mana_regeneration, hero_type, is_visible, items_owned))
            else:
                myUnits.append(unit)
        else:
            if unit_type == "HERO":
                oppHeros.append(Heros(unit_id, unit_type, x, y, attack_range, health, max_health, shield, attack_damage, movement_speed, stun_duration,
                                  gold_value,count_down_1, count_down_2, count_down_3, mana, max_mana, mana_regeneration, hero_type, is_visible, items_owned))
            else:
                oppUnits.append(unit)

    for i in weapons:
        if i.cost < gold:
            potion = i.name
            log(potion, i.cost, gold)
            break
        else:
            potion = ""
    # If roundType has a negative value then you need to output a Hero name, such as "DEADPOOL" or "VALKYRIE".
    # Else you need to output roundType number of any valid action, such as "WAIT" or "ATTACK unitId"
    if round_type < 0:
        print(Hero)
        Hero = "IRONMAN"
    else:
        for hero in myHeros:
            if potion != "" and hero.items < 4:
                print(f"BUY {potion}")
            else:
                if hero.mana > 50 and hero.countDown2 == 0:
                    if hero.hero == "HULK":
                        print("EXPLOSIVESHIELD")
                    else:
                        print(f"FIREBALL 1820 {hero.y}")
                else:
                    if hero.x >= 800:
                        print("MOVE 100 540")
                    else:
                        print("ATTACK_NEAREST HERO")
