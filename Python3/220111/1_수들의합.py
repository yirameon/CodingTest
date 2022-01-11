S = int(input())
num=0
for i in range(1,4294967295):
    num=num+i
    if S==1:
        print(1)
        break
    elif S<num:
        print(i-1)
        break
    elif S==sum:
        print(i)
        break  
