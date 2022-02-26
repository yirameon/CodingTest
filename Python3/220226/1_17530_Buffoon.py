N = int(input())
V = [0]*N
for i in range(N):
    V[i] = int(input())
for j in range(N):
    if V[0] != max(int(V[0]), int(V[j])):
       res = 'N'
       break
    else:
        res = 'S'
print(res)
