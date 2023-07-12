from heapq import heappop,heappush

def solution(numbers):
    answer = [-1] * len(numbers)
    tmp = []
    for i in range(len(numbers)):
        nb = numbers[i]
        while len(tmp)!=0 and tmp[0][0] < nb:
            num , idx = heappop(tmp)
            answer[idx] = nb
        heappush(tmp, [nb,i])
        
    return answer
