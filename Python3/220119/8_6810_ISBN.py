a=int(input())
b=int(input())
c=int(input())
sum=0
A=9780921418
A_list=list(map(int,str(A)))
for i in range(10):
    if (i+1)%2==0:
        sum+=3*A_list[i]
    elif (i+1)%2!=0:
        sum+=A_list[i]
sum+=a+b*3+c
print('The 1-3-sum is %d'%sum)
