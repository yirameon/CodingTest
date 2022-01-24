# n번 interation
# 각 정수형 받아서 A 리스트에 넣기
# A를 정렬해서(내림차순)
# A 배열 내의 인자 출력
A=[]
for i in range(int(input())):
    A.append(int(input()))
A=sorted(A,reverse=True)
for j in range(len(A)):
    print(A[j],end=' ')
