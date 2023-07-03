import heapq

# def solution(book_time):
#     heap = []
#     tmp = []
#     cnt = 0
#     for i in book_time:
#         start = i[0].split(":")
#         s = int(start[0])*60 + int(start[1])
#         end = i[1].split(":")
#         e = int(end[0])*60 + int(end[1]) + 10
#         tmp.append([s,e])
#     tmp.sort(key=lambda x :x[1])
#     heapq.heappush(heap,tmp[0][1])
#     cnt+=1
#     for i in range(1,len(tmp)):
#         if heap[0] <= tmp[i][0] :
#             heapq.heappush(heap,tmp[i][1])
#         else:
#             while len(heap)!=0:
#                 heapq.heappop(heap)
#                 cnt+=1
#             heapq.heappush(heap,tmp[i][1])
            
#     print(tmp)
#     print(heap)
#     print(cnt)
#     return cnt

def solution(book_time):
    tmp = []
    heap = []
    answer = 1
    for i in book_time:
        start = i[0].split(":")
        s = int(start[0])*60 + int(start[1])
        end = i[1].split(":")
        e = int(end[0])*60 + int(end[1]) + 10
        tmp.append([s,e])
    tmp.sort(key=lambda x :x[0])
    for i in range(0,len(tmp)):
        if not heap:
            heapq.heappush(heap,tmp[i][1])
            continue
        if heap[0] <= tmp[i][0] :
            heapq.heappop(heap)
        else:
            answer +=1
        heapq.heappush(heap,tmp[i][1])
    return answer