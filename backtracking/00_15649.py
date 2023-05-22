# N과 M (1)
# complete

import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
n_list = []

def Backtracking():
    if len(n_list) == M:
        print(' '.join(map(str, n_list)))
        return
    for i in range(1, N+1):
        if i not in n_list:
            n_list.append(i)
            Backtracking()
            n_list.pop()

Backtracking()