dp = [[-1, -1] for _ in range(41)]
dp[0] = [1, 0]
dp[1] = [0, 1]

T = int(input())

for _ in range(T):
    N = int(input())
    for i in range(2, N+1):
        dp[i][0] = (dp[i-1][0] + dp[i-2][0])
        dp[i][1] = (dp[i-1][1] + dp[i-2][1])
    print(dp[N][0], dp[N][1])