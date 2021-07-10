n = int(input())
A = list(map(int, input().split()))
dp = [A[0]]

for i in range(1, n):
    # 현재 값 OR 현재값 + 이전 dp값을 계산하며 한칸씩 확인
    dp.append(max(A[i], A[i] + dp[A - 1]))

print(max(dp))