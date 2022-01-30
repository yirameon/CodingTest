from collections import deque
N,M=map(int,input().split())
Map=[]
for _ in range(M):
    Map.append(list(map(int,input())))
# 상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    Q=deque()
    Q.append((x,y))
    while Q:
        x,y=Q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if Map[nx][ny]==0:
                continue
            if Map[nx][ny]==1:
                Map[nx][ny]=Map[x][y]+1
                Q.append((nx,ny))
    return Map[N-1][M-1]
print(bfs(0,0))