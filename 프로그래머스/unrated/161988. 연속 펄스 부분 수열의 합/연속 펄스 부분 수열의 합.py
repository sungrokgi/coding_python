import sys
maxsize = sys.maxsize

def solution(sequence):
    answer = -maxsize 
    pulse = 1
    tmp = []
    for i in range(len(sequence)):
        tmp.append(sequence[i]*pulse)
        pulse*=-1
        
    dp = [[0,0] for i in range(len(tmp))]
    dp[0]= [tmp[0],tmp[0]]
    
    for i in range(1,len(tmp)):
        dp[i][0] = min(tmp[i],dp[i-1][0]+tmp[i])
        dp[i][1] = max(tmp[i],dp[i-1][1]+tmp[i])
    for i in range(len(dp)):
        answer = max(abs(dp[i][0]),abs(dp[i][1]),answer)
    return answer