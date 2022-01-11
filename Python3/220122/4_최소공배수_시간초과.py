T=int(input())
for i in range(T):
    A,B=map(int,input().split())
    if A==B:
        print(A)
    elif A<B:
        j=1
        while 1:
            if B*j%A==0:
                print(B*j)
                break
            elif B*j%A!=0:
                j+=1
    elif A>B:
        j=1
        while 1:
            if A*j%B==0:
                print(A*j)
                break
            elif A*j%B!=0:
                j+=1
    else:
        pass
