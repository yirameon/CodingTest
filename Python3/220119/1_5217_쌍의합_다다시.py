for i in range(int(input())):
    n=int(input())
    print('Pairs for %d:'%n,end=' ')
    for j in range(1,(n+1)//2):
        if j!=1:
            print(',',end=' ')
        print(j,n-j,end='')
    print()
