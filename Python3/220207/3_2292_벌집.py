N=int(input())
i=0
sum=1+6*i
while True:
    if N-1==0:
        print(1)
        break
    i+=1
    sum=sum+6*i
    if sum>=N:
        print(i+1)
        break