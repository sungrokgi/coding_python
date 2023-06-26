import heapq

def solution(targets):
    heap = []
    tmp = 0
    targets.sort(key = lambda x:x[1])
    heapq.heappush(heap, targets[0][1])
    targets.sort()
    for i in range(0,len(targets)):
        if heap[0] > targets[i][0]:
            heapq.heappush(heap, targets[i][1])
        else:
            while len(heap)!=0:
                heapq.heappop(heap)
            tmp+=1
            heapq.heappush(heap, targets[i][1])
    tmp+=1
    answer = tmp
    print(tmp)
    return answer
