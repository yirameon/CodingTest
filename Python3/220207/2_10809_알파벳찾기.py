S=list(input())
A=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
A_num=[-1]*len(A)
i=0
for i in range(len(S)-1,-1,-1):
    if S[i] in A:
        num=A.index(S[i])
        A_num[num]=i
for x in A_num:
    print(x,end=' ')