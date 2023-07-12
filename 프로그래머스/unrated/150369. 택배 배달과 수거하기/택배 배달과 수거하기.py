def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    deliver, pickup = 0,0
    
    for i in range(n):
        deliver += deliveries[i]
        pickup += pickups[i]
        while deliver>0 or pickup>0 :
            deliver -= cap
            pickup -= cap
            answer += (n-i)*2
    return answer