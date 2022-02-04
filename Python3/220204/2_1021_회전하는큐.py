from collections import deque
N,M=map(int,input().split())
A=list(map(int,input().split()))
Q=deque(range(1,N+1))
count=0
for i in A:
    while True:
        if i==Q[0]:
            Q.popleft()
            break
        else:
            if Q.index(i)>len(Q)/2:
                while Q[0]!=i:
                    Q.rotate(-1)
                    count+=1
            else:
                while Q[0]!=i:
                    Q.rotate(1)
                    count+=1
print(count)