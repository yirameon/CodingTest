N=int(input())
A=list(map(int,input().split()))
B=[0 for _ in range(len(A))]
for i in range(len(A)):
    B[i]=A[i]/max(A)*100
print(sum(B)/len(B))