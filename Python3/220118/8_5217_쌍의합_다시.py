for i in range(int(input())):
    n=int(input())
    A=1
    print('Pairs for %d:'%n,end=' ')
    for j in range((n-1)//2):
        if j!=0:
            print(',',end=' ')
        print(A,n-A,end='')
        A+=1
       
#수정
for i in range(int(input())):
    n=int(input())
    print('Pairs for %d:'%n,end=' ')
    for j in range(1,(n+1)//2):
        if j!=1:
            print(',',end=' ')
        print(j,n-j,end='')
    print()
