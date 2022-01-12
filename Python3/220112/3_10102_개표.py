a=0
b=0
V=int(input())
C=list(str(input()))
for i in range(V):
    if C[i]=='A':
        a=a+1
    elif C[i]=='B':
        b=b+1

if a>b:
    print('A')
elif a<b:
    print('B')
elif a==b:
    print('Tie')