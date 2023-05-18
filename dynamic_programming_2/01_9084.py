# 동전

import sys

def input():
    return sys.stdin.readline().rstrip()

noc_dic = {}
T = int(input())
N = int(input())
coins = list(map(int, input().split()))
M = int(input())

for coin in coins:
    noc_dic[coin] = 1

while True:
    for noc in noc_dic.keys():
        for n in coins:
            if noc+n in noc_dic:
                noc_dic[noc+n] += 1
            else:
                noc_dic[noc+n] = noc_dic[noc] + 1
