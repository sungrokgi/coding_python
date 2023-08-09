def solution(scores):
    answer = 1
    wanho = scores[0]
    wanho_sum = sum(scores[0])
    scores.sort(key = lambda x: (-x[0],x[1]))
    tmp = 0
    for i in scores:
        if i[0] >wanho[0] and i[1] > wanho[1]:
            return -1
        if i[1] >= tmp:
            if wanho_sum < sum(i):
                answer+=1
            tmp = i[1]         
    return answer