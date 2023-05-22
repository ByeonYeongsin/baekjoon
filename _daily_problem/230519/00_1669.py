# 멍멍이 쓰다듬기

import sys

def input():
    return sys.stdin.readline().rstrip()

X, Y = map(int, input().split())
dp = [[-1 for _ in range(Y-X+1)] for _ in range(Y-X+1)]
dp[1][1] = 1

try:
    for i in range(1, Y-X+1):
        for j in range(Y-X+1):
            if dp[i][j] == -1:
                continue
            else:
                if j-1 >= 1 and i+j-1 < Y-X+1:
                    dp[i+j-1][j-1] = dp[i][j] + 1   
                dp[i+j][j] = dp[i][j] + 1
                dp[i+j+1][j+1] = dp[i][j] + 1
                if i+j+1 == Y-X:
                    raise ValueError
except:
    print(max(dp[Y-X]))
