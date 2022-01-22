list_name=[]
for i in range(int(input())):
    name,d,m,y=input().split()
    list_name.append([name,int(d),int(m),int(y)])
list_name.sort(key=lambda x:(x[3],x[2],x[1]))
print(list_name[-1][0])
print(list_name[0][0])
print(list_name)
