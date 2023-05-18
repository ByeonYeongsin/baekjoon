# 주지수
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
populations = []
for _ in range(N):
    populations.append(list(map, input().split()))
K = int(input())
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2+1):
        populations[]