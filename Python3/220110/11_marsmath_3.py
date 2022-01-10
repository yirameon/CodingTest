T=int(input())
for i in range(T):
    l=list(input().split())
    result=float(l[0])
    for j in range(len(l)):
        if l[j]=='@':
            result=result*3
        elif l[j]=='%':
            result=result+5
        elif l[j]=='#':
            result=result-7
    print('%.2f'%result)