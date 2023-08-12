def solution(arrayA, arrayB):
    answer = 0
    
    gcd_A = arrayA[0]
    gcd_B = arrayB[0]
    
    for n in arrayA[1:]:
        gcd_A = gcd(n, gcd_A)
        
    for n in arrayB[1:]:
        gcd_B = gcd(n, gcd_B)

    if notDiv(arrayA, gcd_B):
        answer = max(answer, gcd_B)
    
    if notDiv(arrayB, gcd_A):
        answer = max(answer, gcd_A)
        
    return answer

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def notDiv(array, gcd):
    for n in array:
        if n % gcd == 0:
            return False
    return True