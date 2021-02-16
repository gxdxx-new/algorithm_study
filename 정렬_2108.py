import sys
from collections import Counter

N = int(sys.stdin.readline())
numList = []
for _ in range(N):
    numList.append(int(sys.stdin.readline()))

avg = round(sum(numList) / len(numList))
print(avg)
numList.sort()

if(N == 1):
    median = numList[0]
else:
    median = numList[N // 2]
print(median)

if(N == 1):
    print(numList[0])
else:
    c = Counter(numList).most_common(2)
    if(c[0][1] == c[1][1]):
        print(c[1][0])
    else:
        print(c[0][0])

print(numList[-1] - numList[0])