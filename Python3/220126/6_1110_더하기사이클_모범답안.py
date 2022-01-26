N=int(input())
n=-1
t=0
while n!=N:
    if n==-1:
        n=N
    n=(n//10+n%10)%10+(n%10)*10
    t+=1
print(t)