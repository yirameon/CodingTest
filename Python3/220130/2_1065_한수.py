N=int(input())
count=0
for a in range(1,N+1):
    if a<100:
        count+=1
    if 99<a<1001:
        # 자리수 쪼개서 배열에 넣고 각 자리수 차이 값 구하기
        A=str(a)
        if int(A[0])-int(A[1])==int(A[1])-int(A[2]):
            count+=1
print(count)