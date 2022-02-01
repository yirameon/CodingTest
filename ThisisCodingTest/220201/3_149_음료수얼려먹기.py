N,M=map(int,input().split())
graph=[]
count=0
for _ in range(N):
    graph.append(list(map(int,input())))

def DFS(i,j):
    global count
    if i<0 or i>=N or j<0 or j>=M:
        pass
    if graph[i][j]==0:
        graph[i][j]=1
        DFS(i-1,j)
        DFS(i+1,j)
        DFS(i,j-1)
        DFS(i,j+1)
        count+=1
    else:
        pass

DFS(0,0)
print(count)