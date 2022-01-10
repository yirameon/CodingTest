T = int(input())
result = []

for i in range(T):
    A,B = map(int, input().split())
    result.append(A+B)

for j in range(T):
    print("Case #%d: %d"%(j+1,result[j]))
