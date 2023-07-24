def solution(n):
    answer = []
    while n:
        b =  n%3
        if b ==0:
            answer.insert(0,4)
            n//=3
            n -=1
        else:
            answer.insert(0,b)
            n//=3
    return ''.join(str(i) for i in answer)
