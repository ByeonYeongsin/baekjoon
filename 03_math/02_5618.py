# 공약수
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
n_list = list(map(int, input().split()))
output_list = []

for i in range(1, min(n_list)+1):
    flag = True
    for num in n_list:
        if num % i != 0:
            flag = False
            break
    if flag == True:
        output_list.append(i)

print(output_list)
for n in output_list: print(n)