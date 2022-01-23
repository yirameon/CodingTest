array=[]
for i in range(int(input())):
    array.append(int(input()))
array=sorted(array,reverse=True)
for j in range(len(array)):
    print(array[j],end=' ')