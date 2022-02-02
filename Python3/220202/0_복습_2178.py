from collections import deque
N,M=map(int,input().split())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def BFS(x,y):
    Q=deque()
    Q.append((x,y))
    while Q:
        x,y=Q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny]==1:
                    graph[nx][ny]=graph[x][y]+1
                    Q.append((nx,ny))
    return graph[N-1][M-1]
print(BFS(0,0))