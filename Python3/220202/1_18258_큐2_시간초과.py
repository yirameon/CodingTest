import sys
from collections import deque
N=int(sys.stdin.readline())
Q=deque()
for _ in range(N):
    A=sys.stdin.readline().split()
    if A[0]=='push':
        Q.append(int(A[1]))
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
