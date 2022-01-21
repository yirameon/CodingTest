def check(arr):
    num=arr.count(0)
    if num==0:
        print('E')
    elif num==1:
        print('A')
    elif num==2:
        print('B')
    elif num==3:
        print('C')
    elif num==4:
        print('D')

for i in range(3):
    arr=list(map(int,input().split()))
    check(arr)
