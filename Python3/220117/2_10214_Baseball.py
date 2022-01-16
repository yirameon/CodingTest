T=int(input())
for i in range(T):
    Y_list=[]
    K_list=[]
    for i in range(9):
        Y,K=map(int,input().split())
        Y_list.append(Y)
        K_list.append(K)
    if sum(Y_list)>sum(K_list):
        print('Yonsei')
    elif sum(Y_list)<sum(K_list):
        print('Korea')
    elif sum(Y_list)==sum(K_list):
        print('Draw')
