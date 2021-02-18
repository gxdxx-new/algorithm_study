dp = [0] * 5001
dp[0] = 99999
dp[1] = 99999
dp[2] = 99999
dp[3] = 1
dp[4] = 99999
dp[5] = 1

N = int(input())
if(N <= 5):
    if(dp[N] == 99999):
        print(-1)
    else:
        print(dp[N])
else:
    for i in range(6, N+1):
        dp[i] = min(dp[i-5], dp[i-3])
        if(dp[i] != 99999):
            dp[i] += 1
    if(dp[N] == 99999):
        print(-1)
    else:
        print(dp[N])