from collections import deque
N,K=map(int,input().split())
Q=deque()
output=[]
for i in range(1,N+1):
    Q.append(i)
for j in range(len(Q)):
    for _ in range(K-1):
        Q.rotate(-1)
    v=Q.popleft()
    output.append(v)
print('<',end='')
for k in output:
    print(k,end='')
    if k!=output[-1]:
        print(', ',end='')
print('>')