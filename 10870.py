dp = [-1] * 21
dp[0] = 0
dp[1] = 1

def fibo(n):
    if(dp[n] != -1):
        return dp[n]
    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]

N= int(input())
result = fibo(N)

print(result)