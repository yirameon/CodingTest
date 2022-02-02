from collections import deque
N,M,v=map(int,input().split())
graph=[[0]*(M+1)for _ in range(N+1)]
visited=[0]*(N+1)
for _ in range(M):
    x,y=map(int,input().split())
    graph[x][y]=graph[y][x]=1

def DFS(v):
    visited[v]=1
    print(v,end=' ')
    for i in range(1,N+1):
        if visited[i]==0 and graph[v][i]==1:
            DFS(i)

def BFS(v):
    Q=deque()
    Q.append(v)
    visited[v]=1
    while Q:
        v=Q.popleft()
        print(v,end=' ')
        for i in range(1,N+1):
            if visited[i]==0 and graph[v][i]==1:
                Q.append(i)
                visited[i]=1
DFS(v)
visited=[0]*(N+1)
print()
BFS(v)
