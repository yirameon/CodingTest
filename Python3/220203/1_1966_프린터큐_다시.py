C=int(input())
for _ in range(C):
    N,M=map(int,input().split())
    important=list(map(int,input().split()))
    index=list(range(len(important)))
    index[M]='Find'
    order=0
    while True:
        if important[0]==max(important):
            order+=1
            if index[0]=='Find':
                print(order)
                break
            else:
                important.pop(0)
                index.pop(0)
        else:
            important.append(important.pop(0))
            index.append(index.pop(0))
