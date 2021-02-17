N = int(input())
numList = []

for _ in range(N):
    x, y = list(map(int, input().split()))
    numList.append((x,y))

sortedNumList = sorted(numList, key=lambda x : (x[1], x[0]))

for i, j in sortedNumList:
    print(i, j)