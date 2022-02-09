n=int(input())
A=[]
op=[]
count=1
T=True
for i in range(n):
    num=int(input())
    while count<=num:
            A.append(count)
            op.append('+')
            count+=1
    if A[-1]==num:
        A.pop()
        op.append('-')
    else:
        T=False
if T==False:
    print('NO')
else:
    for i in op:
        print(i)
