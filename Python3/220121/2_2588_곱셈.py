A,B=int(input()),int(input())
B_arr=[int(i) for i in str(B)]
B_arr.reverse()
for i in range(len(B_arr)):
    print(A*B_arr[i])
print(A*B)