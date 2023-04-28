# 스택
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
stack = []
for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        stack.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if len(stack) == 0:
            print("-1")
        else:
            print(stack.pop(-1))
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        print(0 if len(stack) else 1)
    elif cmd[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print("-1")