# 소수 찾기
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
n_list = list(map(int, input().split()))
count = 0

for num in n_list:
    if num != 2 and num != 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            count += 1
    elif num == 2:
        count += 1
print(count)