import sys
N=sys.stdin.readline()
A=map(int,sys.stdin.readline().split())
A=sorted(A)
M=sys.stdin.readline()
M_list=map(int,sys.stdin.readline().split())

def binary_search(x,A,start,end):
    mid=(start+end)//2
    if start>end:
        return 0
    if x<A[mid]:
        return binary_search(x,A,start,mid-1)
    elif x>A[mid]:
        return binary_search(x,A,mid+1,end)
    elif x==A[mid]:
        return 1

for x in M_list:
    start=0
    end=int(N)-1
    print(binary_search(x,A,start,end))
