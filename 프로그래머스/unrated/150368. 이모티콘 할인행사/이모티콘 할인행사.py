def solution(users, emoticons):
    answer = [0,0]
    n = len(users)
    m = len(emoticons)
    discount = [10,20,30,40]
    alldisc = []
    def realshit(arr,idx,l):
        if idx == l:
            alldisc.append(arr)
            return
        
        for i in range(4):
            realshit(arr+[discount[i]],idx+1,l)
    realshit([],0,m)
    # print(alldisc)
    
    for dis in alldisc:
        kakao_friends = 0
        kakao_earn_money = 0
        
        for user in users:
            user_spend_money = 0
            for i in range(len(dis)):
                if user[0] <= dis[i]:
                    user_spend_money += int(emoticons[i] * (100-dis[i])/100)
            if user[1] <= user_spend_money:
                kakao_friends +=1
            else:
                kakao_earn_money+= user_spend_money
                
        if answer[0] < kakao_friends:
            answer = [kakao_friends,kakao_earn_money]
        elif answer[0] == kakao_friends:
            if answer[1] < kakao_earn_money:
                answer = [kakao_friends,kakao_earn_money]
                   
    return answer