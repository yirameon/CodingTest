n=int(input())
A=list(map(int,input().split()))
print(min(A))
min_A=A[0]
for i in range(len(A)):
    if A[i]<=min_A:
        min_A=A[i]
print(min_A)