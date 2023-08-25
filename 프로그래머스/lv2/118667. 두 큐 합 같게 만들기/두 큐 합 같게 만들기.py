from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 , sum2 = sum(q1), sum(q2)
    
    answer = 0
    limit = len(q1)*4
    print(limit)
    
    if (sum1+sum2) % 2 == 1:
        return -1
    
    while True:
        if sum1 > sum2 :
            a = q1.popleft()
            q2.append(a)
            sum1 -= a
            sum2 += a
            answer += 1
        elif sum1 < sum2:
            a = q2.popleft()
            q1.append(a)
            sum1 += a
            sum2 -= a
            answer += 1
        else:
            break
        if answer == limit :
            return -1
        
    return answer