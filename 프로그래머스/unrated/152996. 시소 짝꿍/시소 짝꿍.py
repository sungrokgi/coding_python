from collections import defaultdict

def solution(weights):
    answer = 0
    dic = defaultdict(int)
    for w in weights:
        dic[w] += 1
    for i,n in dic.items():
        if n>1:
            answer += n*(n-1) //2
        if i *2 in dic:
            answer += dic[i*2] * n
        if i *3 %2 == 0 and i *3//2 in dic:
            answer += dic[i*3//2] * n
        if i *4%3 ==0 and  i *4//3 in dic:
            answer += dic[i*4//3] * n

    return answer