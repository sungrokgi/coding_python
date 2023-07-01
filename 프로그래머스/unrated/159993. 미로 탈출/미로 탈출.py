from collections import deque

def bfs(sx,sy,f,maps):
    r = len(maps[0])
    c = len(maps)
    visited = [[0]*r for i in range(c)]
    mx = [1,-1,0,0]
    my = [0,0,1,-1]
    q = deque()
    q.append([sx,sy,0])
    visited[sy][sx] =1

    while q:
        px,py,dist = q.popleft()
        if maps[py][px] == f:
            return dist
        
        for i in range(4):
            nx,ny = mx[i]+px , my[i]+py
            if 0<=nx<r and 0<=ny<c and maps[ny][nx]!="X" and visited[ny][nx]==0:
                q.append([nx,ny,dist+1])
                visited[ny][nx] = 1
    return -1

def solution(maps):
    answer = 0
    r = len(maps[0])
    c = len(maps)
    for i in range(c):
        for j in range(r):
            if maps[i][j] == "S":
                sx ,sy = j,i
            if maps[i][j] == "L":
                lx ,ly = j,i 

    l = bfs(sx,sy,"L",maps)
    e = bfs(lx,ly,"E",maps)
    if l>-1 and e>-1:
        return l+e
    else:
        return -1