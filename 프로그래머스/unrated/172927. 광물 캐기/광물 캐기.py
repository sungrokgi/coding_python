def solution(picks, minerals):
    answer = 0
    tmp = []
    dia , iron, st = 0,0,0
    for i in range(len(minerals)):
        
        if minerals[i] == "diamond":
            dia +=1
        elif minerals[i] == "iron":
            iron +=1
        else:
            st +=1
        if  i % 5 == 4 or i == len(minerals)-1:
            tmp.append([dia,iron,st])
            dia , iron, st = 0,0,0
    if picks[0]+picks[1]+picks[2] >= len(tmp):
        tmp.sort(key = lambda x : (-x[0] , -x[1]))
    else:
        a = picks[0]+picks[1]+picks[2]
        tmp = tmp[0:a:]
        tmp.sort(key = lambda x : (-x[0] , -x[1]))
    i = 0
    while picks[0] and i < len(tmp):
        answer +=  tmp[i][0]+tmp[i][1] +tmp[i][2]
        picks[0] -=1
        i+=1 

    while picks[1] and i < len(tmp):
        answer += 5*tmp[i][0]+tmp[i][1] +tmp[i][2]
        picks[1] -=1
        i+=1

    while picks[2] and i < len(tmp):
        answer += 25*tmp[i][0]+ 5*tmp[i][1] +tmp[i][2]
        picks[2] -=1
        i+=1

    return answer