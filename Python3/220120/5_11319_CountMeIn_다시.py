M=['A','E','I','O','U','a','e','i','o','u']
S=int(input())
for i in range(S):
    A=str(input())
    v=c=0
    for j in A:
        if j in M:
            v+=1
        elif j.isalpha():
            c+=1
    print(c,v)