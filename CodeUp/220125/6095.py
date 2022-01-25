n=int(input())
A=[[0 for j in range(19)] for i in range(19)] # List Comprehension
for i in range(n):
    x,y=map(int,input().split())
    A[x-1][y-1]=1
for i in range(19):
    for j in range(19):
        print(A[i][j],end=' ')
    print()