# 암호 만들기

import sys

def input():
    return sys.stdin.readline().rstrip()

def Backtracking(i):
    if len(a) == L:
        break
    else:
        for j in range(i, C):
            if al[j] not in re:
                re.append(al[j])
                Backtracking(j)
                re.pop()

L, C = map(int, input().split())
