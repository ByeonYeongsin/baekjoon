# 암벽 등반
import sys

def input():
    return sys.stdin.readline().rstrip()

n, T = map(int, input().split())
rock_walls = []

for _ in range(n):
    rock_walls.append(list(map(int, input().split())))

rock_walls.sort()
now_loc = [0, 0]
count = 0
while True:
    if now_loc[1] == T:
        break
    for rock in rock_walls:
        dif = 0
        if now_loc 