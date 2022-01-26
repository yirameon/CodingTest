A=[]
for i in range(5):
    A.append(int(input()))
print(sum(A)//5)
A.sort()
print(A[2])