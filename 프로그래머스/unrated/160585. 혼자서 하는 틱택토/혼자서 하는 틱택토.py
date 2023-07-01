def solution(board):
    
    o,x = 0,0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                o+=1
            elif board[i][j] == "X":
                x+=1          
    if o<x:
        return 0
    if o> x+1:
        return 0
    if o ==0 and x == 0:
        return 1
    
    owin , xwin = 0,0
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0]== "O":
            owin +=1
        elif board[0][0] == "X":
            xwin +=1
    if board[1][1] == board[2][0] and board[1][1] == board[0][2]:
        if board[1][1]== "O":
            owin +=1
        elif board[1][1] == "X":
            xwin +=1
    for i in range(3):
        if board[i][0]==board[i][1] and board[i][0]==board[i][2]:
            if board[i][1]== "O":
                owin +=1
            elif board[i][1] == "X":
                xwin +=1
        if board[0][i]==board[1][i] and board[1][i]==board[2][i]:
            if board[1][i]== "O":
                owin +=1
            elif board[1][i] == "X":
                xwin +=1
    if owin == 0 and xwin ==0:
        return 1
    if xwin ==0 and owin>0:
        if x<o:
            return 1
    if owin ==0 and xwin>0:
        if x == o :
            return 1
    return 0
            
        