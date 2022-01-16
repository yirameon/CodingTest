A=B=100
n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    if x==y:
        continue
    elif x>y:
        B=B-x
    elif x<y:
        A=A-y
print(A)
print(B)
