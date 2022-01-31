from collections import deque
def BFS(graph,start,visited):
    Q=deque([start])
    visited[start]=True
    while Q:
        v=Q.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                Q.append(i)
                visited[i]=True
                print(Q)

graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited=[False]*9
print(BFS(graph,1,visited))