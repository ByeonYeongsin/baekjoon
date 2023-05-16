# 다이어트

import sys

def input():
    return sys.stdin.readline().rstrip()

G = int(input())

now_weight = 2
while True:
    old_weight = now_weight + 1
    while True:
        if now_weight*now_weight - old_weight*old_weight == G:

        now_weight += 1
    old_weight += 1