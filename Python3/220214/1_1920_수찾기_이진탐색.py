from sys import stdin, stdout
n = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
m = stdin.readline()
M = map(int, stdin.readline().split())

def binary(x,N,start,end):
    if start>end:
        return 0
    mid=(start+end)//2
    if x==N[mid]:
        return 1
    elif x<N[mid]:
        return binary(x,N,start,mid-1)
    else:
        return binary(x,N,mid+1,end)

for x in M:
    start=0
    end=len(N)-1
    print(binary(x,N,start,end))
