import sys
N=int(sys.stdin.readline())
N_list=sorted(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
M_list=map(int,sys.stdin.readline().split())

def binary_search(x,N_list,start,end):
    mid=(start+end)//2
    if start>end:
        return 0
    if x<N_list[mid]:
        return binary_search(x,N_list,start,mid-1)
    elif x>N_list[mid]:
        return binary_search(x,N_list,mid+1,end)
    elif x==N_list[mid]:
        return N_list[start:end+1].count(x)

N_dic={}
for x in N_list:
    if x not in N_dic:
        N_dic[x]=binary_search(x,N_list,0,len(N_list)-1)
print(' '.join(str(N_dic[i]) if i in N_dic else '0' for i in M_list))
