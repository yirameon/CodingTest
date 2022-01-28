N,M=map(int,input().split())
result=0
for i in range(N):
    A=list(map(int,input().split()))
    min_value=min(A)
    result=max(result,min_value)
print(result)