M,N=int(input()),int(input())
A=[]
for i in range(1,N+1):
    if M<=i**2<=N:
        A.append(i**2)
if len(A)==0:
    print('-1')
else:
    print(sum(A))
    print(A[0])
