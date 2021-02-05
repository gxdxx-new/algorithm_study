numList = list(input().split('-'))

totalSum = 0

for i in range(len(numList)):
    numList[i] = numList[i].split('+')

for i in range(len(numList[0])):
    totalSum += int(numList[0][i])

for i in range(1,len(numList)):
    for j in range(len(numList[i])):
        totalSum -= int(numList[i][j])

print(totalSum)