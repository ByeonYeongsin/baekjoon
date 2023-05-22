# N과 M (4)

import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
n_list = []

def Backtracking(i):
    if len(n_list) == M:
        print(' '.join(map(str, n_list)))
        return
    for j in range(i, N+1):
        n_list.append(j)
        Backtracking(j)
        n_list.pop()

Backtracking(1)