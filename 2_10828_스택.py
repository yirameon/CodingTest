import sys
N=int(input())
A=[]
for _ in range(N):
    cmd=sys.stdin.readline().split()
    if cmd[0]=='push':
        A.append(int(cmd[1]))
    elif cmd[0]=='pop':
        if len(A)==0:
            print(-1)
        else:
            print(A.pop())
    elif cmd[0]=='size':
        print(len(A))
    elif cmd[0]=='empty':
        if len(A)==0:
            print(1)
        else:
            print(0)
    elif cmd[0]=='top':
        if len(A)==0:
            print(-1)
        else:
            print(A[-1])
