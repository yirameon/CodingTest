# 집합자료형이용
N=int(input())
N_list=set(map(int,input().split()))
M=int(input())
M_list=list(map(int,input().split()))

for j in M_list:
    if j in N_list:
        print('yes',end=' ')
    else:
        print('no',end=' ')