S=int(input())
num=0
for i in range(1,S):
    num=num+i
    if S<=num:
        print(i-1)
        break