A,B=sorted(map(int,input().split()))
if A==B:
    print('0')
else:
    print(B-A-1)
    for i in range(A+1,B):
        print(i,end=' ')