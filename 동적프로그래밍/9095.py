# dfs
# T = int(input())

# def dp(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     elif n == 3:
#         return 4
#     else:
#         return dp(n-1)+dp(n-2)+dp(n-3)

# for i in range(T):
    
#     n = int(input())
#     print(dp(n))  

#dp
import sys
T = int(sys.stdin.readline())

dp = [0]*11 # n이 11보다 작으므로

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

for j in range(T):
    print(dp[int(sys.stdin.readline())])