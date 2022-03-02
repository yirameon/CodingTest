import sys
A,B=list(sys.stdin.readline().split())
A_list=list(A)
B_list=list(B)
A_back=[]
B_back=[]
A_num=str()
B_num=str()
for i in range(len(A_list)):
    A_back.append(int(A_list[i]))
for ii in range(len(A_back)-1,-1,-1):
    A_num+=str(A_back[ii])
for j in range(len(B_list)):
    B_back.append(int(B_list[j]))
for jj in range(len(B_back)-1,-1,-1):
    B_num+=str(B_back[jj])
print(max(A_num,B_num))
