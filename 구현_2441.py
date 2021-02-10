N = int(input())
for i in range(N, 0, -1):
    star = "*" * i
    print(star.rjust(N))