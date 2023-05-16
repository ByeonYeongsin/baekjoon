# 거의 소수

import sys

def input():
    return sys.stdin.readline().rstrip()

def check_decimal(n):
    flag = True
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break
    return flag

A, B = map(int, input().split())
n_list = []
for i in range(2, int(B**(1/2)+1)):
    if check_decimal(i):
        now_num = i
        j = 2
        while True:
            now_num ** j
            j += 1
            if now_num >= A and now_num <= B:
                n_list.append(now_num)
            elif now_num > B:
                break

print(len(n_list))