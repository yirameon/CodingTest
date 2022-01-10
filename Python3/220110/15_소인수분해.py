T=int(input())
while T!=1:
    for i in range(2,T+1):
        if T%i==0:
            print(i)
            T=T//i
            break