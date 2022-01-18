N=int(input())
for i in range(N):
    X,Y=map(int,input().split())
    if X<Y:
        print('NO BRAINS')
    elif X>=Y:
        print('MMM BRAINS')