N = int(input())

X = N
count = 0

while True:
    if(X < 10):
        first = 0
        second = X
    else:
        first = X // 10
        second = X % 10

    X = second*10 + (first + second)%10
    count += 1
    if(X == N):
        print(count)
        break