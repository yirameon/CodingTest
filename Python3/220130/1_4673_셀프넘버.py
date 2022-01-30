natural=[]
generated=[]
for i in range(1,10001):
    natural.append(i)
    for j in str(i):
        i+=int(j)
    generated.append(i)
num=sorted(set(natural)-set(generated))
for k in range(len(num)):
    print(num[k])
