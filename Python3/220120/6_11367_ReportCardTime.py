for i in range(int(input())):
    A,B=map(str,input().split())
    B=int(B)
    if 97<=B<=100:
        print(A,'A+')
    elif 90<=B<=96:
        print(A,'A')
    elif 87<=B<=89:
        print(A,'B+')
    elif 80<=B<=86:
        print(A,'B')
    elif 77<=B<=79:
        print(A,'C+')
    elif 70<=B<=76:
        print(A,'C')
    elif 67<=B<=69:
        print(A,'D+')
    elif 60<=B<=66:
        print(A,'D')
    elif 0<=B<=59:
        print(A,'F')
