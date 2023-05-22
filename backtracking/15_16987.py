# 계란으로 계란치기

import sys
import numpy as np

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
global count
count = 0

def check_square(ans_list):
    for i in range(N-1):
        for j in range(M-1):
            if ans_list[i][j] == 1 and ans_list[i][j+1] and ans_list[i+1][j] + ans_list[i+1][j+1]:
                return True
    return False

def calculate_matrix_sum(ans_list):
    sum = 0
    for i in range(N):
        for j in range(M):
            sum += ans_list[i][j]
    return sum

def Backtracking(ans_list, i):
    if calculate_matrix_sum(ans_list) == i:
        if check_square(ans_list) == False:
            global count 
            count = 1
            return
    for x in range(N):
        for y in range(M):
            ans_list[x][y] = 1
            Backtracking(ans_list, i)
            ans_list[x][y] = 0
    

for i in range(N*M+1):
    ans_list = [[0 for _ in range(M)] for _ in range(N)]
    Backtracking(ans_list, i)
print(count)