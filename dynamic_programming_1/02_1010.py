#######

# 다리 놓기
import sys

def input():
    return sys.stdin.readline().rstrip()

dp = [[0 for _ in range(30)] for __ in range(30)]
dp[0][0] = 1
for i in range(1, 31):
    dp[i][0] = 1
    for j in range(1, 31):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j] 

N = int(input())
for _ in range(N):
    n, m = map(int, input().split())
    print(dp[n][m])