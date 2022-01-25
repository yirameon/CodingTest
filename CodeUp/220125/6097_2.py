# 격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
# 막대를 놓는 방향(d:가로는 0, 세로는 1)과
# 막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,
# 격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.
h,w=map(int,input().split())

n=int(input())

A=[[0 for i in range(w+1)]for j in range(h+1)]

for i in range(n):
    l,d,x,y=map(int,input().split())
    l=l-1
    if d==0: # 가로
        # (현재 x좌표 + 막대 길이) 값이 격자판의 가로 길이보다 길면?
        if (x+l)<=h:
            for j in range(y,y+l+1):
                A[x][j]=1
        elif (x+l)>h:
            for j in range(y,h+1):
                A[x][j]=1
    elif d==1: # 세로
        # (현재 y좌표 + 막대 길이) 값이 격자판의 세로 길이보다 길면?
        if (y+l)<=w:
            for j in range(x,x+l+1):
                A[j][y]=1
        elif (y+1)>w:
            for j in range(x,w+1):
                A[j][y]=1


for i in range(1,h+1):
    for j in range(1,w+1):
        print(A[i][j],end=' ')
    print()