A,B,C=int(input()),int(input()),int(input())
result=A*B*C
result_list=list(map(int,str(result)))
for i in range(10):
    print(result_list.count(i))