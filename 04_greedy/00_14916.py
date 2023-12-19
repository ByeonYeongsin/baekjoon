# 거스름돈
import sys

def input():
    return sys.stdin.readline().rstrip()

m = int(input())
count = 0
while m >= 2:
    if m % 5 == 0:
        count += int(m/5)
        break
    else:
        count += 1
        m -= 2

if m == 1: print("-1") 
else: print(count)