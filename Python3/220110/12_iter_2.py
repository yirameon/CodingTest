N=int(input())
for i in range(N):
    S,text=map(str,input().split())
    S=int(S)
    for j in range(0,len(text)):
        print(text[j]*S,end='')
    print()