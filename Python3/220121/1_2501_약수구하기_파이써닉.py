N,K=map(int,input().split())
A=[i for i in range(1,N+1) if N%i==0]
print(0 if len(A)<K else A[K-1])