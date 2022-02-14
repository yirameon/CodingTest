# 계수정렬
N=int(input())
N_list=[0]*1000001
for i in input().split():
    N_list[int(i)]=1
M=int(input())
M_list=list(map(int,input().split()))

for j in M_list:
    if N_list[j]==1:
        print('yes',end=' ')
    else:
        print('no',end=' ')