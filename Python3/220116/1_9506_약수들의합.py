while True:
    n=int(input())
    A=[1]
    if n==-1:
        break
    else:
        for i in range(2,n):
            if n%i==0:
                A.append(i)
        result=str(n)+' = 1'
        if n==sum(A):
            for j in range(1,len(A)):
                result+=' + '+str(A[j])
            print(result)
        elif n!=sum(A):
            print('%d is NOT perfect.'%n)
