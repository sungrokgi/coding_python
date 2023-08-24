def solution(cards):
    answer  = 0
    c = []
    visited = [0 for i in range(len(cards))]
    for i, card in enumerate(cards):
        
        if visited[i] == 0:
            cnt =1
            visited[i] = 1
            idx = card-1
            while True:
                if visited[idx] ==0:
                    cnt+=1
                    visited[idx] = 1
                    idx = cards[idx] -1
                else:
                    break
            c.append(cnt)
    c.sort()
    if len(c) >=2:
        return c[-1] *c[-2]
    else:
        return 0


# from collections import defaultdict

# def solution(cards):
#     answer = 0
#     dic = defaultdict(set)
#     for i in range(1,len(cards)+1):
#         dic[i].add(cards[i-1])
#     for i in range(1,len(cards)+1):
#         if dic[i] not in dic[cards[i-1]]:
#             dic[cards[i-1]].update(dic[i])
#             dic[i].update(dic[cards[i-1]])
#             for j in dic[i]:
#                 dic[j].update(dic[i])
#     # print(dic)
#     # print()
             
#     tmp = 0
#     tmp_1 = 0
#     tmp_list = []
#     for i in range(1,len(dic)+1):
#         if dic[i] == tmp_list:
#             del dic[i]
#         if len(dic[i]) >tmp:
#             tmp = len(dic[i])
#             tmp_list = dic[i]
#             del dic[i]
#         if len(dic[i]) >= tmp_1:
#             tmp_1 = len(dic[i])
            
#     return tmp*tmp_1