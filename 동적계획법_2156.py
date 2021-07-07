n = int(input())

wine = []
dp = []

for i in range(n):
    wine.append(int(input()))

dp.append(wine[0])

if(n >= 2):
    dp.append(wine[0] + wine[1])

if(n >= 3):
    dp.append(max(wine[1] + wine[0], wine[2] + wine[0], wine[2] + wine[1]))

for i in range(3, n):
    dp.append(max(dp[i - 1], dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i]))

print(max(dp))