import sys

stack = [-1] * 10000

top = -1

N = int(sys.stdin.readline())

for i in range(N):
    n = sys.stdin.readline().split()
    count = 0
    if(n[0] == 'push'):
        stack[top + 1] = int(n[1])
        top += 1
    elif(n[0] == 'pop'):
        print(stack[top])
        if(top != -1):
            top -= 1
    elif(n[0] == 'size'):
        if(top != -1):
            print(top + 1)
        else:
            print(0)
    elif(n[0] == 'empty'):
        if(top == -1):
            print(1)
        else:
            print(0)
    elif(n[0] == 'top'):
        if(top != -1):
            print(stack[top])
        else:
            print(-1)