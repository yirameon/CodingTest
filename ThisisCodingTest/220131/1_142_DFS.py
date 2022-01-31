def DFS(graph,v,visited):
    visited[v]=9 # 현재 노드 v에 대해 방문처리
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            DFS(graph,i,visited)

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

visited=[False]*len(graph)
DFS(graph,1,visited)
