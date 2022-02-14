def binary_search(array,start,end,M):
    while start<=end:
        total=0
        mid=(start+end)//2
        for x in array:
            if x>mid:
                total+=(x-mid)
        if total>M:
            start=mid+1
        elif total<M:
            end=mid-1
        else:
            break
    return mid
N,M=map(int,input().split())
array=list(map(int,input().split()))
array=sorted(array)
result=binary_search(array,0,max(array),M)
print(result)
