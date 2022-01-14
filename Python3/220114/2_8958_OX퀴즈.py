T=int(input())
A=list()
B=num=0
for i in range(T):
    A=list(str(input()))
    for i in range(len(A)):
        if A[i]=='O':
            num+=1
            B+=num
        elif A[i]!='O':
            num=0
    print(B)
    num=B=0
