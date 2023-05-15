# 배열 합치기
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
n_list = []
for i in range(2):
    now_list = list(map(int, input().split()))
    for now_num in now_list:
        n_list.append(now_num)
n_list.sort()
print(*n_list)