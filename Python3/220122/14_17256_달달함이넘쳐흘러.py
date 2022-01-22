A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=[]
C.append(B[0]-A[2])
C.append(B[1]//A[1])
C.append(B[2]-A[0])
for i in range(3):
    print(C[i],end=' ')