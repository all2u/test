import math
import sys


def log(*x):
    print(*x, file=sys.stderr)

    
class Entity:
    def __init__(self,_id=None, x=0, y=0,shield_life=None, is_controlled=None):
        self._id = _id
        self.x = x
        self.y = y
        self.shield_life = shield_life
        self.is_controlled = is_controlled
        
    def __repr__(self):
        return f"{self.x} {self.y}"
    
    def __str__(self):
        return f"{self.x} {self.y}"
    
    def distance(self, other):
        return math.sqrt(abs(other.x - self.x)**2+abs(other.y - self.y)**2)


class Hero(Entity):
    def __init__(self,_id, x, y, shield_life, is_controlled):
        super().__init__(_id, x, y, shield_life, is_controlled)
        self.target = None
    

        
class Monster(Entity):
    def __init__(self,_id, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for):
        super().__init__(_id, x, y, shield_life, is_controlled)
        self.health = health
        self.vx = vx
        self.vy = vy
        self.near_base = near_base
        self.threat_for = threat_for


def bestTarget(hero, monsters):
    inf = 5000
    target = None
    for monster in monsters:
        # log(base,base.distance(monster),targets)
        if monster not in targets and base.distance(monster)<=5000:
            d = hero.distance(monster)
            # log(d)
            if d<inf:
                inf = d
                target = monster
    #targets.append(target)
    hero.target = target

# base_x: The corner of the map representing your base
base_x, base_y = [int(i) for i in input().split()]
hero_x = base_x+1000 if base_x==0 else base_x-1000
hero_y = base_y+1000 if base_y==0 else base_y-1000
heroes_per_player = int(input())  # Always 3
# log(base_x, base_y)
base = Entity(None, base_x, base_y)

# game loop
while True:
    # health: Your base health
    # mana: Ignore in the first league; Spend ten mana to cast a spell
    health, mana = [int(j) for j in input().split()]
    oppHealth, oppMana = [int(j) for j in input().split()]
    entity_count = int(input())  # Amount of heros and monsters you can see
    monsters = []
    myHeros = []
    oppHeros = []
    for i in range(entity_count):
        # _id: Unique identifier
        # _type: 0=monster, 1=your hero, 2=opponent hero
        # x: Position of this entity
        # shield_life: Ignore for this league; Count down until shield spell fades
        # is_controlled: Ignore for this league; Equals 1 when this entity is under a control spell
        # health: Remaining health of this monster
        # vx: Trajectory of this monster
        # near_base: 0=monster with no target yet, 1=monster targeting a base
        # threat_for: Given this monster's trajectory, is it a threat to 1=your base, 2=your opponent's base, 0=neither
        _id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for = [int(j) for j in input().split()]
        if _type == 0:
            monsters.append(Monster(_id, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for))
        elif _type == 1:
            myHeros.append(Hero(_id, x, y, shield_life, is_controlled))
        elif _type == 2:
            oppHeros.append(Hero(_id, x, y, shield_life, is_controlled))
    targets=[]
    
    for hero in myHeros:
        targets.append(bestTarget(hero, monsters))
        # log(hero.target)
        
    for i in range(heroes_per_player):
        me = myHeros[i]
        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)


        # In the first league: MOVE <x> <y> | WAIT; In later leagues: | SPELL <spellParams>;
        if me.target:
            print(f"MOVE {me.target}")
        else:
            print(f"MOVE {hero_x} {hero_y}")
