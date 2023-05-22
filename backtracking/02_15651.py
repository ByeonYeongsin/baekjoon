# N과 M (3)
# complete

import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
n_list = []

def Backtracking():
    if len(n_list) == M:
        print(' '.join(map(str, n_list)))
        return
    for i in range(1, N+1):
        n_list.append(i)
        Backtracking()
        n_list.pop()

Backtracking()