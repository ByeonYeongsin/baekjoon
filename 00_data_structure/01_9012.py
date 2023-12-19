# 9012
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
for _ in range(N):
    string = input()
    stack = []
    for s in string:
        if s == '(':
            stack.append(0)
        elif s == ')':
            if len(stack) == 0:
                print("NO")
                break
            stack.pop(0)
    else:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")