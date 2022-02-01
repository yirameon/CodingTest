N=int(input())
array=[]
for i in range(N):
    a=input().split()
    array.append((a[0],int(a[1])))
array=sorted(array,key=lambda x:x[1])
for a in array:
    print(a[0],end=' ')