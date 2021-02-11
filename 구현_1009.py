T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    if(b > 4):
        b = b%4
        if(b == 0):
            b = 4
    if((a ** b) % 10 == 0):
        print(10)
    else:
        print((a ** b) % 10)