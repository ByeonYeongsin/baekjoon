# N과 M (1)

import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

def Backtracking():
    if len(s) == m:
        return
    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            Backtracking()
            s.pop()

N, M = map(int, input().split())
N_list = [i for i in range(1, N+1)]
a = combinations(N_list, M)
print(N_list)

# print('\n'.join(combinations(N_list, M)))
