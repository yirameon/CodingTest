N=int(input())
count=0
for h in range(N+1):
    for m in range(60):
        for s in range(60):
            A=str(h)+str(m)+str(s)
            if A.count('3')>0:
                count+=1
print(count)