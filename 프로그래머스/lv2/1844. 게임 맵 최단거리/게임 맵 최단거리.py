from collections import deque
def solution(maps):
    m = len(maps)
    n = len(maps[0])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    answer = 0
    visited = [[0]*n for _ in range(m)]
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            if  0<= x+dx[i] <m and 0<= y+dy[i] <n and maps[x+dx[i]][y+dy[i]] !=0:
                if visited[x+dx[i]][y+dy[i]] == 0:
                    q.append((x+dx[i],y+dy[i]))
                    visited[x+dx[i]][y+dy[i]] = visited[x][y] + 1
    if visited[-1][-1] == 0:
        return -1
    return visited[-1][-1]