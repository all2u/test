import sys
import math
from enum import Enum
import random

def log(*x):
    print(*x, file=sys.stderr)


class CubeCoord:
    directions = [[1, -1, 0], [1, 0, -1 ], [0, 1, -1], [-1, 1, 0], [-1, 0, 1], [0, -1, 1]]

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    """@Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + x;
        result = prime * result + y;
        result = prime * result + z;
        return result;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        CubeCoord other = (CubeCoord) obj;
        if (x != other.x)
            return false;
        if (y != other.y)
            return false;
        if (z != other.z)
            return false;
        return true;"""

    def neighbor(self,orientation, distance=1):
        nx = self.x + self.directions[orientation][0] * distance
        ny = self.y + self.directions[orientation][1] * distance
        nz = self.z + self.directions[orientation][2] * distance
        return CubeCoord(nx, ny, nz)

    def distanceTo(self, dst):
        return (abs(self.x - dst.x) + abs(self.y - dst.y) + abs(self.z - dst.z)) / 2

    def __str__(self):
        return f"{self.x} {self.y} {self.z}"

    def getOpposite(self):
        oppositeCoord = CubeCoord(-self.x, -self.y, -self.z)
        return oppositeCoord


class Cell:
    def __init__(self, cell_index, richness, neighbors):
        self.cell_index = cell_index
        self.richness = richness
        self.neighbors = neighbors
        
    def __repr__(self):
        return f"Id: {self.cell_index} Rich: {self.richness} Neigb: {self.neighbors}"

class Tree:
    def __init__(self, cell_index, size, is_mine, is_dormant):
        self.cell_index = cell_index
        self.size = size
        self.is_mine = is_mine
        self.is_dormant = is_dormant
        
    def __repr__(self):
        return f"{self.cell_index} {size} {is_dormant}"

class ActionType(Enum):
    WAIT = "WAIT"
    SEED = "SEED"
    GROW = "GROW"
    COMPLETE = "COMPLETE"

class Action:
    def __init__(self, type, target_cell_id=None, origin_cell_id=None):
        self.type = type
        self.target_cell_id = target_cell_id
        self.origin_cell_id = origin_cell_id

    def __str__(self):
        if self.type == ActionType.WAIT:
            return 'WAIT'
        elif self.type == ActionType.SEED:
            return f'SEED {self.origin_cell_id} {self.target_cell_id}'
        else:
            return f'{self.type.name} {self.target_cell_id}'

    @staticmethod
    def parse(action_string):
        split = action_string.split(' ')
        if split[0] == ActionType.WAIT.name:
            return Action(ActionType.WAIT)
        if split[0] == ActionType.SEED.name:
            return Action(ActionType.SEED, int(split[2]), int(split[1]))
        if split[0] == ActionType.GROW.name:
            return Action(ActionType.GROW, int(split[1]))
        if split[0] == ActionType.COMPLETE.name:
            return Action(ActionType.COMPLETE, int(split[1]))

class Game:
    def __init__(self):
        self.day = 0
        self.nutrients = 0
        self.board = []
        self.trees = []
        self.possible_actions = []
        self.my_sun = 0
        self.my_score = 0
        self.opponent_sun = 0
        self.opponent_score = 0
        self.opponent_is_waiting = 0

    def cellIndex(self, index):
        for cells in self.board:
            if cells.cell_index == index:
                return cells
    
    def scoring(self):
        myScore = self.my_score + self.my_sun / 3
        hisScore = self.opponent_score + self.opponent_sun / 3
        mytrees = [x for x in self.trees if x.is_mine]
        opptrees = [x for x in self.trees if not x.is_mine]
        if myScore > hisScore:
            diff = myScore - hisScore
            if diff > 5:
                return 1.0 + (diff - 5) * 0.001
            else:
                return 0.5 + 0.5 * diff / 5
        elif myScore < hisScore:
            diff = hisScore - myScore
            if diff > 5:
                return -1.0 - (diff - 5) * 0.001
            else:
                return -0.5 - 0.5 * diff / 5
        else:
            if len(mytrees) > len(opptrees):
                return 0.25 + myScore * 0.001
            elif len(mytrees) < len(opptrees):
                return -0.25 + myScore * 0.001
            else:
                return myScore * 0.001
    
    def BstNeighbors(self, tree):
        pass
    
    def compute_next_action(self):
        log(self.scoring())
        if len(self.possible_actions) > 1:
            action = None
            for actions in self.possible_actions:
                if actions.type == ActionType.COMPLETE and actions.target_cell_id == self.selectBestTree():
                    action = actions
                    log(action)
                    
                if actions.type == ActionType.GROW and actions.target_cell_id == self.selectBestGrow():
                    action = actions
                    log(action)
                    break
                if actions.type == ActionType.SEED and actions.origin_cell_id == self.selectBestSeed():
                    action = actions
                    log(action)
                    
            return action
        return self.possible_actions[0]
    
    def selectBestTree(self):
        board = sorted(self.board, key=lambda x: x.richness, reverse=True)
        trees = [x for x in self.trees if x.is_mine]
        bstTree = []
        for cells in board:
            index = cells.cell_index
            bstTree += [tree for tree in trees if tree.cell_index == index]
        log("COMPLETE :",bstTree)
        return bstTree[0].cell_index
    
    def selectBestGrow(self):
        
        board = sorted(self.board, key=lambda x: x.richness, reverse=True)
        trees = [x for x in self.trees if x.is_mine and x.size < 3 and not x.is_dormant]
        bstGrow = []
        for cells in board:
            index = cells.cell_index
            bstGrow += [tree for tree in trees if tree.cell_index == index]
        bstGrow = sorted(bstGrow, key=lambda x: x.size, reverse=True)
        log("GROW :",bstGrow)
        return bstGrow[0].cell_index
    
    def selectBestSeed(self):
        board = sorted(self.board, key=lambda x: x.richness, reverse=True)
        trees = [x for x in self.trees if x.is_mine and not x.is_dormant and x.size > 0]
        bstSeed = trees
        """for tree in trees:
            log(self.cellIndex(tree.cell_index))
            if tree.cell_index == self.cellIndex(tree.cell_index).cell_index:"""
        log("SEED :",bstSeed)
        return bstSeed[0].cell_index
        
    
    


number_of_cells = int(input())
game = Game()
for i in range(number_of_cells):
    cell_index, richness, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]
    game.board.append(Cell(cell_index, richness, [neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5]))

while True:
    _day = int(input())
    game.day = _day
    nutrients = int(input())
    game.nutrients = nutrients
    sun, score = [int(i) for i in input().split()]
    game.my_sun = sun
    game.my_score = score
    opp_sun, opp_score, opp_is_waiting = [int(i) for i in input().split()]
    game.opponent_sun = opp_sun
    game.opponent_score = opp_score
    game.opponent_is_waiting = opp_is_waiting
    number_of_trees = int(input())
    game.trees.clear()
    for i in range(number_of_trees):
        inputs = input().split()
        cell_index = int(inputs[0])
        size = int(inputs[1])
        is_mine = inputs[2] != "0"
        is_dormant = inputs[3] != "0"
        game.trees.append(Tree(cell_index, size, is_mine, is_dormant))

    number_of_possible_actions = int(input())
    game.possible_actions.clear()
    for i in range(number_of_possible_actions):
        possible_action = input()
        log(possible_action)
        game.possible_actions.append(Action.parse(possible_action))

    print(game.compute_next_action())