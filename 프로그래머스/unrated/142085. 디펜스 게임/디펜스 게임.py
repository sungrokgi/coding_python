import heapq
def solution(n, k, enemy):
    e = 0
    h = []
    if k >= len(enemy):
        return len(enemy)
    for i in range(len(enemy)):
        heapq.heappush(h,-enemy[i])
        e+= enemy[i]
        if e>n:
            if k==0:
                return i
            e -= (-heapq.heappop(h))
            k-=1      
            
    return i+1