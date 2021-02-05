N = int(input())
P = list(map(int,input().split()))
min_time = 0
time = 0

P.sort()

for i in P:
    min_time += (time + i)
    time += i

print(min_time)