import sys
A=[]
N=int(input())
for _ in range(N):
    C=list(sys.stdin.readline().split())    # command
    if C[0]=='push_front':
        A.append(0)
        for i in range(len(A)-1,0,-1):
            A[i]=A[i-1]
        A[0]=C[1]
    elif C[0]=='push_back':
        A.append(C[1])
    elif C[0]=='pop_front':
        if len(A)!=0:
            print(A.pop(0))
        else:
            print(-1)
    elif C[0]=='pop_back':
        if len(A)!=0:
            print(A.pop())
        else:
            print(-1)
    elif C[0]=='size':
        print(len(A))
    elif C[0]=='empty':
        if len(A)==0:
            print(1)
        else:
            print(0)
    elif C[0]=='front':
        if len(A)!=0:
            print(A[0])
        else:
            print(-1)
    elif C[0]=='back':
        if len(A)!=0:
            print(A[-1])
        else:
            print(-1)
