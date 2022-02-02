from collections import deque
N=int(input())
Q=deque([])
for _ in range(N):
    A=input().split()
    if A[0]=='push':
        A[1]=int(A[1])
        Q.append(A[1])
    elif A[0]=='pop':
        if len(Q)!=0:
            v=Q.popleft()
            print(v)
        elif len(Q)==0:
            print(-1)
    elif A[0]=='size':
        print(len(Q))
    elif A[0]=='empty':
        if len(Q)==0:
            print(1)
        elif len(Q)!=0:
            print(0)
    elif A[0]=='front':
        if len(Q)!=0:
            print(Q[0])
        elif len(Q)==0:
            print(-1)
    elif A[0]=='back':
        if len(Q)!=0:
            print(Q[-1])
        elif len(Q)==0:
            print(-1)
    