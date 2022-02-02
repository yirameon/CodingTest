from collections import deque
C=int(input())
for _ in range(C):
    N,M=map(int,input().split())
    impt=[]
    impt=list(map(int,input().split()))
    Q=deque(impt)
    count=0
    while True:
        impt_temp=sorted(impt,reverse=True)
        print('Q:',Q)
        print('impt:',impt)
        print('count:',count)
        if Q[0]==impt_temp[0]:
            count=1
            break
        else:
            count+=1
            if Q[0]==max(impt):
                Q.popleft()
            else:
                Q.append(Q.popleft())
    A=M-count+1
    if A<=0:
        print(A+len(Q))
    else:
        print(A)