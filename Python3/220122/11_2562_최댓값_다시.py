A=[]
for i in range(1,10):
    A.append(int(input()))
print(max(A))
print(A.index(max(A))+1)