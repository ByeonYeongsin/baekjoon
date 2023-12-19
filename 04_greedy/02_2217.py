# 로프
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
w_list = []

for _ in range(N):
    w_list.append(int(input()))

w_list.sort(reverse=True)
max_weight=0
# print(w_list)
for i in range(len(w_list)):
    now_weight = w_list[i] * (i+1)
    if max_weight < now_weight:
        max_weight = now_weight
print(max_weight)
