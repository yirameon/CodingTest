T=int(input())
if T%10!=0:
    print('-1')
elif T//300==0:
    A=0
    if T//60==0:
        B=0
        C=T//10
        print(A,B,C)
    elif T//60>0:
        T_1=T%60
        B=T//60
        C=T_1//10
        print(A,B,C)
elif T//300>0:
    A=T//300
    T_2=T%300
    if T_2//60==0:
        B=0
        C=T_2//10
        print(A,B,C)
    elif T_2//60>0:
        B=T_2//60
        T_3=T_2%60
        C=T_3//10
        print(A,B,C)
