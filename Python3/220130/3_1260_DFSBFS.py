# 1260번 DFS와 BFS / 실버 2
from collections import deque
N,M,v=map(int,input().split())
graph=[[0]*(N+1) for _ in range(N+1)]
visited_dfs=[0]*(N+1)
visited_bfs=[0]*(N+1)
for _ in range(M):
    x,y=map(int,input().split())
    graph[x][y]=graph[y][x]=1

def dfs(v):
    visited_dfs[v]=1
    print(v,end=' ')
    for i in range(1,N+1):
        if visited_dfs[i]==0 and graph[v][i]==1:
            dfs(i)

def bfs(v):
    Q=deque()
    Q.append(v)
    visited_bfs[v]=1
    while Q:
        v=Q.popleft()
        print(v,end=' ')
        for i in range(1,N+1):
            if visited_bfs[i]==0 and graph[v][i]==1:
                Q.append(i)
                visited_bfs[i]=1

dfs(v)
print()
bfs(v)