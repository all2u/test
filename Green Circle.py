import sys
import math


class Person:
    def __init__(self, name, parent, birth, death, religion, gender):
        self.name = name
        self.parent = parent
        self.birth = birth
        self.isdead = False if death == "-" else True
        self.religion = religion
        self.gender = gender


class MonarchNode:
    def __init__(self, name,age, gender, religion):
        self.name = name
        self.age = age
        self.alive = True
        self.gender = 0 if gender=="M" else 1
        self.religion = religion
        self.children = []

    def __repr__(self):
        return str(f"{self.name}")


class Monarchy:
    monarchy_root = None

    def bfs(self, node, name):
        if not node:
            return
        if name == node.name:
            return node
        for child in node.children:
            node = self.bfs(child, name)
            if node:
                return node

    def birth(self, child, parent,age, gender, religion):
        if self.monarchy_root:
            parent_node = self.bfs(self.monarchy_root, parent)
            parent_node.children.append(MonarchNode(child,age, gender, religion))
        else:
            self.monarchy_root = MonarchNode(child,age, gender, religion)

    def death(self, name):
        node = self.bfs(self.monarchy_root, name)
        if node:
            node.alive = False

    def get_order_of_successions(self):
        monarchs = []

        def bft(monarch):
            if not monarch:
                return
            if monarch.alive:
                monarchs.append(monarch)
            for child in monarch.children:
                child.children = sorted(child.children,key = lambda x: x.age and x.gender)
                bft(child)
        print(monarchs)
        bft(self.monarchy_root)
        return monarchs


desc = ["KingGeorgeVI - 1895 1952 Anglican M",
          "QueenElizabethII KingGeorgeVI 1926 - Anglican F",
          "CharlesPrinceofWales QueenElizabethII 1948 - Anglican M",
          "PrinceWilliamDukeofCambridge CharlesPrinceofWales 1982 - Anglican M",
          "PrinceGeorgeofCambridge PrinceWilliamDukeofCambridge 2013 - Anglican M",
          "PrincessCharlotteofCambridge PrinceWilliamDukeofCambridge 2015 - Anglican F",
          "PrinceHenryofWales CharlesPrinceofWales 1984 - Anglican M",
          "PrinceEdwardEarlofWessex QueenElizabethII 1964 - Anglican M",
          "PrinceAndrewDukeofYork QueenElizabethII 1960 - Anglican M",
          "PrincessBeatriceofYork PrinceAndrewDukeofYork 1988 - Anglican F",
          "PrincessEugenieofYork PrinceAndrewDukeofYork 1990 - Anglican F",
          "JamesViscountSevern PrinceEdwardEarlofWessex 2007 - Anglican M",
          "LadyLouiseWindsor PrinceEdwardEarlofWessex 2003 - Anglican F",
          "AnnePrincessRoyal QueenElizabethII 1950 - Anglican F",
          "PeterPhillips AnnePrincessRoyal 1977 - Anglican M",
          "SavannahPhillips PeterPhillips 2010 - Anglican F",
          "IslaPhillips PeterPhillips 2012 - Anglican F",
          "ZaraTindall AnnePrincessRoyal 1981 - Anglican F",
          "MiaTindall ZaraTindall 2014 - Anglican F",
          "PrincessMargaretCountessofSnowdon KingGeorgeVI 1930 2002 Anglican F",
          "DavidArmstrong-Jones2ndEarlofSnowdon PrincessMargaretCountessofSnowdon 1961 - Anglican M",
          "CharlesArmstrong-JonesViscountLinley DavidArmstrong-Jones2ndEarlofSnowdon 1999 - Anglican M",
          "LadyMargaritaArmstrong-Jones DavidArmstrong-Jones2ndEarlofSnowdon 2002 - Anglican F",
          "LadySarahChatto PrincessMargaretCountessofSnowdon 1964 - Anglican F",
          "SamuelChatto LadySarahChatto 1996 - Anglican M",
          "ArthurChatto LadySarahChatto 1999 - Anglican M"]


n = 26

#n = int(input())
Family = []
m = Monarchy()
for i in range(n):
    inputs = desc[i].split()
    name = inputs[0]
    parent = inputs[1]
    birth = int(inputs[2])
    death = inputs[3]
    religion = inputs[4]
    gender = inputs[5] 
    if parent == "-":
        parent = None
    m.birth(name, parent, birth,gender, religion)
    if death != "-":
        m.death(name)
    # Family.append(Person(name,parent,birth,death,religion,gender))

orders = m.get_order_of_successions()
print(orders)
"""for order in orders:
    order.children = sorted(order.children,key = lambda x: x.birth)
    print(order.name, order.birth, order.children, file=sys.stderr)
for order in orders:
    print(order.name, order.age, order.children, file=sys.stderr)
    print(order)"""
