T=int(input())
A=list(map(int,input().split()))
num=0
for i in range(len(A)):
    if T==A[i]:
        num+=1
print(num)