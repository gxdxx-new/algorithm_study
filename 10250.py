T = int(input())
result = []
for _ in range(T):
    H, W, N = map(int,input().split())
    if(N % H == 0):
        Y = (H)
        X = (N // H)
        result.append(int(str(Y) + str(X).zfill(2)))
    else:
        Y = (N % H)
        X = (N // H + 1)
        result.append(int(str(Y) + str(X).zfill(2)))
for i in range(T):
    print(result[i])