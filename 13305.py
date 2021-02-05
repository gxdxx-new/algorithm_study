import sys

input = sys.stdin.readline()

N = int(input())

distance = list(map(int, input().split()))

cost = list(map(int, input().split()))

result = 0

minCost = cost[0]

for i in range(0, N-1):
    if(minCost > cost[i]):
        minCost = cost[i]
    result += minCost * distance[i]

print(result)