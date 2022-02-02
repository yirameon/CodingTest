from collections import deque
N=int(input())
Q=deque()
for i in range(1,N+1):
    Q.append(i)
while True:
    if len(Q)==0:
        break
    else:
        if len(Q)==1:
            print(Q[0])
        Q.popleft()
        Q.rotate(-1)
