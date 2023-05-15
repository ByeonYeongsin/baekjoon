# 블로그

import sys

def input():
    return sys.stdin.readline().rstrip()

N, X = map(int, input().split())
visitors_list = list(map(int, input().split()))
max_visitor = sum(visitors_list[:X])
max_visi_num = 1

for i in range(N-X):
    if visitors_list[i] < visitors_list[X+i]:
        max_visitor = max_visitor - visitors_list[i] + visitors_list[X+i]
    elif visitors_list[i] == visitors_list[X+i]:
        max_visi_num += 1

if max_visitor == 0:
    print("SAD")
else:
    print(max_visitor)
    print(max_visi_num)
