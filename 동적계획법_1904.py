N = int(input())

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
if(N == 1):
    print(dp[1])
elif(N == 2):
    print(dp[2])
else:
    for i in range(3, N + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746 #수가 너무 커지기 때문에 출력값에서만 %하지 않고 더하면서 %
    print(dp[N])