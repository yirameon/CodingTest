A,B=sorted(map(int,input().split()))
if A==B:
    print(0)
else:
    print(B-A-1)
print(' '.join(map(str,range(A+1,B))))
