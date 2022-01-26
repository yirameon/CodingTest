# 맨 아래 가장 오른쪽에 도착한 경우
# 더 이상 움직일 수 없는 경우
# 먹이를 찾은 경우
# 더 이상 이동하지 않고 그곳에 머무른다고 가정함
A=[[0 for i in range(10)] for j in range(10)]
for k in range(10):
    A[k]=list(map(int,input().split()))
i,j=1,1
while True:
    if A[j][i]==0:
        A[j][i]=9
    elif A[j][i]==2:
        A[j][i]=9
        break
    if A[j+1][i]==1 and A[j][i+1]==1:
        break
    if A[j][i+1]!=1:
        i+=1
    elif A[j+1][i]!=1:
        j+=1
for x in range(10):
    for y in range(10):
        print(A[x][y],end=' ')
    print()
