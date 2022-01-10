T=int(input())
i=0
j=0
m=list(input().split())
length=len(m)

def con(a):
    if a == '@':
        return result*3
    elif a == '%':
        return result+5
    elif a == '#':
        return result-7
    else:
        return float(a)

while j<T:
    j+=1
    while i<length:
        result=con(m[i])
        i+=1
    print('%0.2f'%result)
