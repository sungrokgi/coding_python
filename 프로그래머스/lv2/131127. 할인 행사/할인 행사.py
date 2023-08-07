from collections import Counter

def solution(want, number, discount):
    start , end , answer = 0, 10 ,0
    for i in range(len(discount) - 9):
        answer+=1
        cnt = Counter(discount[start:end])
        for w,n in zip(want,number):
            if cnt[w]!= n:
                answer-=1
                break
        start+=1
        end+=1
    return answer