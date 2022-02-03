T=int(input())
for _ in range(T):
    stack=[]
    A=list(input())
    for x in A:
        if x=='(':
            stack.append(x)
        else:
            if len(stack)!=0 and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(x)
                break
    if len(stack)==0:
        print('YES')
    else:
        print('NO')