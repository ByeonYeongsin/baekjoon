# 소수

import sys

def input():
    return sys.stdin.readline().rstrip()

n1 = int(input())
n2 = int(input())
n_list = [i for i in range(n1, n2+1)]

for i in range(2, n2):
    for num in n_list:
        if num > i and num % i == 0:
            n_list.remove(num)  

if n_list:
    print(sum(n_list))
    print(n_list[0])
else:
    print("-1")