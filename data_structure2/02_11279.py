# 최대 힙
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = []
for _ in range(N):
    num = int(input())
    if num != 0:
        arr.append(num)
    else:
        if arr:
            arr.sort()
            print(arr.pop(-1))
        else:
            print(0)