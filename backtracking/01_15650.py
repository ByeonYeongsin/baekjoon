# N과 M (2)
# complete

import sys

def input():
    return sys.stdin.readline().rstrip()

n_list = []
N, M = map(int, input().split())

def Backtracking(start):
    if len(n_list) == M:
        print(' '.join(map(str, n_list)))
        return
    for i in range(start, N+1):
        if i not in n_list:
            n_list.append(i)
            Backtracking(i)
            n_list.pop()

Backtracking(1)