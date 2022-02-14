# 이진탐색
def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None
    
N=int(input())
N_list=list(map(int,input().split()))
M=int(input())
M_list=list(map(int,input().split()))
N_list_sort=sorted(N_list)

for i in M_list:
    result=binary_search(N_list_sort,i,0,N-1)
    if result!=None:
        print('yes',end=' ')
    else:
        print('no',end=' ')