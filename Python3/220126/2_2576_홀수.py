A,B=[],[]
sum=0
for i in range(7):
    A.append(int(input()))
for j in range(7):
    if A[j]%2!=0:
        sum+=A[j]
        B.append(A[j])
if len(B)==0:
    print(-1)
else:
    print(sum)
    print(min(B))