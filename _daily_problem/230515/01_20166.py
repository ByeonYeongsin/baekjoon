# 문자열 지옥에 빠진 호석
import sys

def input():
    return sys.stdin.readline().rstrip()

def search(alp, now_x, now_y, str, i):
    if alp[now_x][now_y] == str[i]

N, M, K = map(int, input().split())
alp = []
for _ in range(N):
    alp.append(input())

for _ in range(K):
    str = input()
    count = 0
    for i in range(N):
        for j in range(M):
            now_char = alp[N][M]
