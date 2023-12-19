# 알바생 강호
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
tip_list = []
for _ in range(N):
    tip_list.append(int(input()))
tip_list.sort(reverse=True)
total_tip = 0
for i in range(N):
    total_tip += max((tip_list[i]-(i)), 0)

print(total_tip)