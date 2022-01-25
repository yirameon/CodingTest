A=[[0 for j in range(19)] for i in range(19)]
for i in range(19):
    A[i]=list(map(int,input().split()))
n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    x=x-1
    y=y-1
    for j in range(19):
        if A[j][y]==0:
            A[j][y]=1
        else:
            A[j][y]=0
        if A[x][j]==0:
            A[x][j]=1
        else:
            A[x][j]=0
for a in range(19):
    for b in range(19):
        print(A[a][b],end=' ')
    print()