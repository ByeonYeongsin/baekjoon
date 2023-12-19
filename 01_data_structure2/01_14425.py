# 문자열 집합
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
s = []
cnt = 0
for _ in range(N):
    s.append(input())
for _ in range(M):
    if input() in s: cnt = cnt+1

print(cnt)