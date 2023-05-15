# 피로도
import sys

def input():
    return sys.stdin.readline().rstrip()

A, B, C, M = map(int, input().split())

fatigue = 0
work = 0

for _ in range(24):
    if fatigue + A < M:
        work += B
        fatigue += A
    else:
        fatigue -= C
        if fatigue < 0:
            fatigue = 0

print(work)