import sys
A=[]
K=int(input())
for _ in range(K):
    num=int(sys.stdin.readline())
    if num==0:
        A.pop()
    else:
        A.append(num)
print(sum(A))