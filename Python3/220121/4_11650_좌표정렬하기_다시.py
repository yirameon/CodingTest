arr=[]
for i in range(int(input())):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x:(x[0],x[1]))
for j in arr:
    print(str(j[0])+' '+str(j[1]))