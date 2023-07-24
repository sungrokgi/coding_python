def solution(n):
    
    n//=2
    dp = [0]*(n+1)
    dp[1] = 3
    dp[2] = 11
    for i in range(3,n+1):
         dp[i] = (dp[i-1]*3 +2*sum(dp[:i-1]) +2) % 1000000007
    return dp[n]