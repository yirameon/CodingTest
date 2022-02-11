X=int(input())
i=1
while X>i:
    X-=i
    i+=1
if i%2==0:
    a=X
    b=i-X+1
else:
    a=i-X+1
    b=X
print('{}/{}'.format(a,b))
