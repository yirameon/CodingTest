words=input().upper()
uni=list(set(words))
A=[]
for x in uni:
    c=words.count(x)
    A.append(c)
if A.count(max(A))>1:
    print('?')
else:
    max_index=A.index(max(A))
    print(uni[max_index])
