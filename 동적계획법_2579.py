import sys

count = int(sys.stdin.readline().rstrip())
stair = []
for i in range(count):
    stair.append(int(sys.stdin.readline().rstrip()))

dp = []
dp.append(stair[0])
if(count >= 2):
    dp.append(stair[1] + dp[0])
if(count >= 3):
    dp.append(stair[2] + max(dp[0], stair[1]))

for i in range(3, count):
    dp.append(stair[i] + max(stair[i-1] + dp[i-3], dp[i-2]))

print(dp[-1])