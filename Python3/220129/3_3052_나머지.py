A=[]
for i in range(10):
    A.append(int(input())%42)
A=set(A)
print(len(A))