# # 신기한 소수

import sys
import math
import time

# def input():
#     return sys.stdin.readline().rstrip()

# N = int(input())

# n_list = [2, 3, 5, 7]
# start = time.time()
# for i in range(1, N):
#     next_n_list = []
#     for now_num in n_list:
#         for j in range(1, 11, 2):
#             now_check_num = int(str(now_num) + str(j))
#             check_flag = True
#             for k in range(2, now_check_num):
#                 if now_check_num % k == 0:
#                     check_flag = False
#                     break
#             if check_flag == True:
#                 next_n_list.append(now_check_num)
#         n_list = next_n_list.copy()

# print('\n'.join(map(str, n_list)))
# end = time.time()
# print(end - start)


#DFS
import sys
sys.setrecursionlimit(10000)
n = int(input())
def isPrime(num):
    for i in range(2, int(num**(1/2))+1):
        if num%i==0:
            return False
    return True

def dfs(number):
    if not isPrime(number):
        return
    if len(str(number)) == n:
        print(number)
    for i in range(1,10,2):
        dfs(number*10 + i)
    return

start = time.time()
for i in [2,3,5,7]:
    dfs(i)
end = time.time()
print(end - start)