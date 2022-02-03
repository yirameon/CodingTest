from collections import deque
N,M=map(int,input().split())
graph=[]
count=1
for _ in range(N):
    graph.append(list(map(int,input())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def BFS(x,y):
    Q=deque()
    Q.append((x,y))
    while Q:
        x,y=Q.popleft()
        for a in range(4):
            nx=x+dx[a]
            ny=y+dy[a]
            if nx<0 or nx>=N or ny<0 or ny<=M:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                Q.append((nx,ny))
                graph[nx][ny]=graph[x][y]+1
BFS(0,0)
print(graph[N-1][M-1])