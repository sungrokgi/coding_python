def solution(sequence, k):
    answer = []
    l,r = 0,0
    dist = 1000000000
    index = 0
    tmp = 0
    if k in sequence:
        i = sequence.index(k)
        return [i,i]
    else:
        for a,b in enumerate(sequence):
            r = a
            tmp +=b
            if tmp == k:
                answer.append([l,r])
                if r-l < dist:
                    dist = r-l
                    index = len(answer)-1
                tmp-= sequence[l]
                l+=1
            elif tmp> k:
                while tmp >k:
                    tmp -= sequence[l]
                    l+=1
                if tmp == k:
                    answer.append([l,r])
                    if r-l < dist:
                        dist = r-l
                        index = len(answer)-1
                    tmp -= sequence[l]
                    l+=1           
    return answer[index]