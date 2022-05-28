import sys
from typing import List, Tuple
import itertools

def log(*x):
    print(*x, file=sys.stderr)

def compute_min_subseq_length(subsequences):
    permutations = list(itertools.permutations(subsequences))
    min_length = 60
    c=0
    seq = []
    for permutation in permutations:
        sequence = "".join(str(permutation[0]).split(", "))[1:n+1]
        # log(sequence)
        for i in range(1, len(permutation)):
            j = 0
            while j < len(sequence):
                subsequence = "".join(str(permutation[i]).split(", "))[1:n+1]
                # check if the subsequence is contained within the sequence
                if sequence.find(subsequence) != -1:
                    break
                # check if there is a partial match
                end_index = len(sequence) - j
                if sequence[j:] == subsequence[:end_index]:
                    sequence += subsequence[end_index:]
                j += 1
            # check if there is no match
            if j == len(sequence):
                sequence += subsequence
        
        min_length = min(min_length, len(sequence))
        if len(sequence) <= min_length and sequence not in seq:
            seq.append(sequence)
    return (sorted(seq,key=lambda x:int(x)))[0]


"""x = int(input())
n = int(input())"""
x=10
n=2


comb = list(itertools.product(range(x), repeat = n))
perm = compute_min_subseq_length(comb)
log(perm)