# 도로의 개수

import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
K = int(input())
broken_roads = []
dp = [[0 for _ in range(M)] for _ in range(N)]


for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1
    if y1 > y2:
        x1, y1, x2, y2 = x2, y2, x1, y1
    
for i in range(N):
    dp[i][0] = 1
for i in range(M):
    dp[0][i] = 1

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print(dp[i-1][j])
        print(dp[i][j-1])
        print(dp[i][j])
        for broken_road in broken_roads:
            if broken_road[2] == i and broken_road[3] == j:
                if broken_road[0] == i-1:
                    dp[i][j] =- dp[i-0][j]
                elif broken_road[1] == j-1:
                    dp[i][j] =- dp[i][j-1]

print(dp)