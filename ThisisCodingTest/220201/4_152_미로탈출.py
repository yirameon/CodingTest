from collections import deque
N,M=map(int,input().split())
graph=[]
count=1
for _ in range(N):
    graph.append(list(map(int,input())))

di=[-1,1,0,0]
dj=[0,0,-1,1]

def BFS(i,j):
    Q=deque()
    Q.append((i,j))
    while Q:
        i,j=Q.popleft()
        for a in range(4):
            ni=i+di[a]
            nj=j+dj[a]
            if ni<0 or ni>=N or nj<0 or nj>=M:
                continue
            if graph[ni][nj]==0:
                continue
            if graph[ni][nj]==1:
                Q.append((ni,nj))
                graph[ni][nj]=graph[i][j]+1
                
BFS(0,0)
print(graph[N-1][M-1])
