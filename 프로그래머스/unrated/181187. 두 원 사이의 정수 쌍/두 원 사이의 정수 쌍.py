def solution(r1, r2):
    answer = 0
    i , j = r2, r1
    for x in range(0,r2):
        while (i*i + x*x) > r2*r2:
            i -=1
        while (j-1)**2 + x*x >= r1*r1 and j-1:
            j -=1
        answer += i-j +1
    answer = answer*4
    return answer

