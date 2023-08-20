from collections import deque

def solution(n, roads, sources, destination):
    visited = [-1] * (n+1)
    graph = [[] for i in range(n+1)]
    
    for i,j in roads:
        graph[i].append(j)
        graph[j].append(i)
    q = deque()
    q.append(destination)
    visited[destination] = 0
    while q:
        tmp = q.popleft()
        for node in graph[tmp]:
            if visited[node] == -1:
                visited[node] = visited[tmp] +1
                q.append(node)

    return [visited[i] for i in sources]
