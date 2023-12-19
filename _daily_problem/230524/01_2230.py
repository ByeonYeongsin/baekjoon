# 수 고르기
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
n_list = []


for _ in range(N):
    n_list.append(int(input()))
n_list.sort()
dif = n_list[-1] - n_list[0] + 1
for i in range(N-1):
    for j in range(N-1, i, -1):
        now_dif = n_list[j] - n_list[i]
        if now_dif < dif and now_dif >= M:
            dif = now_dif
        if now_dif < M:
            break
print(dif)