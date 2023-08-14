from collections import Counter

def solution(topping):
    answer = 0
    b1 = Counter(topping)
    b2 = set()
    for i in topping:
        b1[i] -=1
        if b1[i] == 0:
            b1.pop(i)
        b2.add(i)
        if len(b1) == len(b2):
            answer+=1
    return answer