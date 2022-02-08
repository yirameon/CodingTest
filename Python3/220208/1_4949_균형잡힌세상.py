import sys
while True:
    S=list(sys.stdin.readline().rstrip())
    A=list()
    flag=True
    for x in S:
        if x=='(' or x=='[':
            A.append(x)
        elif x==')':
            if A and A[-1]=='(':
                A.pop()
            else:
                flag=False
                break
        elif x==']':
            if A and A[-1]=='[':
                A.pop()
            else:
                flag=False
                break
    if S[0]=='.':
        break
    print('yes' if flag and not(A) else 'no')
