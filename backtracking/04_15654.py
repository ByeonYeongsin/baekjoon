# N과 M (5)

import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()
c_list = []

def Backtracking():
    if len(c_list) == M:
        print(' '.join(map(str, c_list)))
        return
    for i in n_list:
        if i not in c_list:
            c_list.append(i)
            Backtracking()
            c_list.pop()

Backtracking()