N=int(input())
N_list=list(map(int,input().split()))
d=[0]*100
d[0]=N_list[0]
d[1]=max(N_list[0],N_list[1])
for i in range(2,N):
    d[i]=max(d[i-1],d[i-2]+N_list[i])
print(d[N-1])