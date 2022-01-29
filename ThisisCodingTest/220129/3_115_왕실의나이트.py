A=input()
count=0
a=int(ord(A[0]))-96
b=int(A[1])
print(a,b)
if 3<=a<=6:
    count+=2
elif a<3 or a>6:
    count+=1
if 3<=b<=6:
    count+=2
elif b<3 or b>6:
    count+=1
print(count)