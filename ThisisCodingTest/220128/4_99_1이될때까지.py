N,K=map(int,input().split())
i=0
while True:
    if N==1:
        break
    if N%K!=0:
        N-=1
    elif N%K==0:
        N=N//K
    i+=1
print(i)