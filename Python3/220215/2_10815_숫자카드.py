import sys
N=sys.stdin.readline()
N_list=sorted(map(int,sys.stdin.readline().split()))
M=sys.stdin.readline()
M_list=map(int,sys.stdin.readline().split())

def binary_search(x,N_list,start,end):
    mid=(start+end)//2
    if start>end:
        return 0
    if x<N_list[mid]:
        return binary_search(x,N_list,start,mid-1)
    elif x>N_list[mid]:
        return binary_search(x,N_list,mid+1,end)
    else:
        return 1

for x in M_list:
    print(binary_search(x,N_list,0,int(N)-1),end=' ')