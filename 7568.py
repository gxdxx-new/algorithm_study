N = int(input())

array = []

for _ in range(N):
    array.append(list(map(int, input().split())))

for i in array:
    rank = 1
    for j in array:
        if(i[0] < j[0] and i[1] < j[1]):
            rank += 1
    print(rank, end=' ')