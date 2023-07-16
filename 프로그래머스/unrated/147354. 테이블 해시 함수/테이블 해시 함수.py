def solution(data, col, row_begin, row_end):
    answer = 0
    tmp = 0
    data.sort(key = lambda x : (x[col-1],-x[0]))
    for i in range(row_begin-1,row_end):
        for j in range(len(data[i])):
            tmp += (data[i][j] % (i+1))
        answer ^= tmp
        tmp =  0
    return answer