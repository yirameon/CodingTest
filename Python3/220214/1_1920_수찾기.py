import sys
def binary_search(x,N,start,end):
    mid=(start+end)//2
    if start>end:
        return 0
    if x==N[mid]:
        return 1
    elif x<N[mid]:
        return binary_search(x,N,start,mid-1)
    else:
        return binary_search(x,N,mid+1,end)

N=sys.stdin.readline()
N_list=list(sys.stdin.readline().split())
M=sys.stdin.readline()
M_list=list(sys.stdin.readline().split())
N_list=sorted(N_list)

for x in M_list:
    start=0
    end=len(N_list)-1
    print(binary_search(x,N_list,start,end))