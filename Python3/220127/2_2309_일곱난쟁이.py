# (받은 input의 총 합)-(a+b)=100
A=[]
for _ in range(9):
    A.append(int(input()))
sum_A=sum(A)
for i in range(8):
    for j in range(i+1,9):
        if sum_A-(A[i]+A[j])==100:
            a=A[i]
            b=A[j]
            break
A.remove(a)
A.remove(b)
A.sort()
for i in A:
    print(i)