N=int(input())
A=list(map(str,input().split()))
for i in range(N):
    for j in range(N):
        if A[i]=='R':
            if i!=1:
                i+=1
        elif A[i]=='L':
            if i!=5:
                i-=1
        elif A[i]=='U':
            if j!=1:
                j+=1
        elif A[j]=='D':
            if j!=1:
                j-=1
print(j,i)
