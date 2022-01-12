N=int(input())
cute_list=list()
while N%2==0:
    N=int(input())
for i in range(N):
    person=int(input())
    if person==1:
        cute_list.append(1)
    if person==0:
        cute_list.append(0)

if cute_list.count(1)>cute_list.count(0):
    print('Junhee is cute!')
elif cute_list.count(1)<cute_list.count(0):
    print('Junhee is not cute!')
