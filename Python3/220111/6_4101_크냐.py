while 1:
    A,B=map(int, input().split())
    if A>B:
        print('Yes')
    elif A<=B and A!=0 and B!=0:
        print('No')
    elif A==0 and B==0:
        break
