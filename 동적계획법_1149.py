import sys

N = int(sys.stdin.readline())

RGB = []

dp = [[-1] * 3 for _ in range(N)]

for _ in range(N):
    rgb = list(map(int, sys.stdin.readline().split()))
    RGB.append(rgb)

dp[0][0] = RGB[0][0]
dp[0][1] = RGB[0][1]
dp[0][2] = RGB[0][2]

for i in range(1, N):
    dp[i][0] = RGB[i][0] + min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = RGB[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = RGB[i][2] + min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))