from collections import deque

def solution(board):
    answer = 0
    visited = [[0]*len(board[0]) for i in range(len(board))]
    rx , ry = 0, 0
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == "R":
                rx,ry = x,y
                break
                
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    def bfs():
        q = deque()
        q.append((rx,ry))
        visited[rx][ry] = 1
        
        while q:
            px,py = q.popleft()
            if board[px][py] == "G":
                return visited[px][py]
            for i in range(4):
                nx,ny = px, py
                while True:
                    nx,ny = nx+dx[i] , ny+dy[i]
                    if nx<0 or nx>= len(board) or ny <0 or ny>= len(board[0]) or board[nx][ny] == "D":  
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[px][py]+ 1
                    q.append((nx,ny))
        return 0
    answer = bfs() -1
    return answer
