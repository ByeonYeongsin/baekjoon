# N과 M (11)
# complete

import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()
c_list = []
c_dict = {}

def Backtracking():
    if len(c_list) == M:
        k = ' '.join(map(str, c_list))
        if k not in c_dict:
            c_dict[k] = 1
            print(' '.join(map(str, c_list)))
        return
    for i in n_list:
        c_list.append(i)
        Backtracking()
        c_list.pop()

Backtracking()