C=int(input())
for i in range(C):
    N,*arr=list(map(int,input().split()))
    num=0
    mean=sum(arr)/N
    for j in range(len(arr)):
        if arr[j]>mean:
            num+=1
    print('{:.3f}%'.format(num/N*100))