N=int(input())
cute=list()
while N%2==0:
    N=int(input())
for i in range(N):
    ans=int(input())
    if ans==1:
        cute.append(1)
    elif ans==0:
        cute.append(0)

if cute.count(1)>cute.count(0):
    print('Junhee is cute!')
elif cute.count(1)<cute.count(0):
    print('Junhee is not cute!')