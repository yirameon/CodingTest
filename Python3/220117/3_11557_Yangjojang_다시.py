T=int(input())
for i in range(T):
    N=int(input())
    A=[]
    for i in range(N):
        S,L=map(str,input().split())
        A.append([S,int(L)])
    A=sorted(A,key=lambda x: x[1])
    print(A[-1][0])
