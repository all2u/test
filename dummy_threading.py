import sys
import io


input = sys.stdin.readline


def liste_avec_repetition(chiffres, n):
    if n == 0:
        return [[]]
    return [liste + [c] for liste in liste_avec_repetition(chiffres, n - 1) for c in chiffres]


def bin_to_dec(bin_str):
    n = 0
    for b in bin_str:
        n = n * 2 + int(b)
    return n


class Puzzle:
    def __init__(self):
        # on récupère les dimensions
        self.x = int(input())
        self.n = int(input())
        self.chiffres = "".join([str(k) for k in range(self.x)])
        self.nb_combinaisons = self.x ** self.n
        self.crible = {"".join(liste): False for liste in liste_avec_repetition(self.chiffres, self.n)}
        self.atteint = 0
        self.solutions = []

    def backtrack(self, courant, chemin):
        if len(chemin) >= self.n:
            combi = "".join(chemin[-(self.n):])
            if not self.crible[combi]:
                self.crible[combi] = True
                self.atteint += 1
            else:
                return False
        if self.atteint == self.nb_combinaisons:
            self.solutions.append(chemin)
            return True
        for prochain in self.chiffres:
            chemin_suivant = chemin + prochain
            if len(chemin_suivant) >= self.n:
                etat_backup = self.crible["".join(chemin_suivant[-self.n:])]
                etat_atteint = self.atteint
            rep = self.backtrack(prochain, chemin + prochain)
            if rep:
                return True
            if len(chemin_suivant) >= self.n:
                self.crible["".join(chemin_suivant[-self.n:])] = etat_backup
                self.atteint = etat_atteint
            print(etat_backup)
        return False

    def solve(self):
        # print(self.crible)
        self.backtrack("1", "0" * self.n)
        print(min(self.solutions, key=bin_to_dec))


if __name__ == "__main__":
    p = Puzzle()
    p.solve()
