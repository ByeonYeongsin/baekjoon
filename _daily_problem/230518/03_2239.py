# 스도쿠

import sys

def input():
    return sys.stdin.readline().rstrip()

def check_sdk(sdk, i, j):
    return False

sdk = []

for _ in range(9):
    sdk.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if sdk[i][j] == 0:
            for k in range(k):
                sdk[i][j] = k
                if check_sdk 