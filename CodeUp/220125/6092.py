n=int(input())
a=list(map(int,input().split()))
A=[0]*23
for i in range(n):
    A[a[i]-1]+=1
for j in range(len(A)):
    print(A[j],end=' ')
