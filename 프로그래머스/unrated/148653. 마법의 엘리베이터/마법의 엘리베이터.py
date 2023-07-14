def solution(storey):
    answer = 0
    while storey:
        tmp = storey% 10
        if tmp < 5:
            answer+=tmp
        elif tmp>5:
            answer += (10 - tmp)
            storey +=10
        else:
            if (storey//10) % 10  >= 5 :
                storey +=10
            answer += tmp
        storey = storey//10
    
    return answer