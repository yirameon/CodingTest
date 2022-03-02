A,B=input().split()
def back(n):
    n=n[::-1]
    return int(n)
print(max([back(A),back(B)]))