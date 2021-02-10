def w(a, b, c):
    if(a <= 0 or b <= 0 or c <= 0):
        return 1

    if (dp[a][b][c] != 0):
        return dp[a][b][c]

    if(a > 20 or b > 20 or c > 20):
        if(dp[20][20][20] == 0):
            dp[20][20][20] = w(20, 20, 20)
        return dp[20][20][20]

    if(a < b < c):
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]

    else:
        dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return dp[a][b][c]

# 3차원 배열 선언
dp = [[[0] * 21 for i in range(21)] for j in range(21)]
while True:
    a, b, c = map(int, input().split())
    if(a == -1 and b == -1 and c == -1):
        break
    print('w(' + str(a) + ',', str(b) + ',', str(c) + ') =', w(a, b, c))
#for(int i = 0; i < 21; i++)
#	{
#	    for (int j = 0; j < 21; j++)
#		{
#			for (int k = 0; k < 21; k++)
#			{
#				array[i][j][k] = 0;
#			}
#		}
#   }