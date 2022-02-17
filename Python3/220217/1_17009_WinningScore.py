A=[]
for i in range(6):
    A.append(int(input()))
apple=A[0]*3+A[1]*2+A[2]
banana=A[3]*3+A[4]*2+A[5]
if banana<apple:
    print('A')
elif banana>apple:
    print('B')
else:
    print('T')
