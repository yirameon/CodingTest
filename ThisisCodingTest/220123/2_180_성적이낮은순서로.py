B=[]
for i in range(int(input())):
    A=input().split()
    B.append(A)
B=sorted(B,key=lambda x:x[1])
for j in range(len(B)):
    print(B[j][0],end=' ')