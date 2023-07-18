def solution(k, tangerine):
    answer = 0
    tmp = {}
    for i in tangerine:
        if i not in tmp:
            tmp[i] = 1
        else:
            tmp[i] +=1
    val = list(tmp.values())
    val.sort(reverse = True)
    for i in val:
        if k > 0:
            k-= i
            answer+=1
    return answer