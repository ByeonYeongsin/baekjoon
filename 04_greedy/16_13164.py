# 13164
# 행복유치원

import sys

def input():
    return sys.stdin.readline().rstrip()

N,K = map(int, input().split())
h = list(map(int, input().split()))
 
arr = []
 
for i in range(N-1):
    a = h[i+1] - h[i]
    arr.append(a)
 
arr.sort()
cost = 0
 
for i in range(N-K):
    cost += arr[i]
 
print(cost)