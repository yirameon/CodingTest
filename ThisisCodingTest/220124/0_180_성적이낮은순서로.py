# 몇명 받을 건지 n에 받아서 iteration
# (이름,성적) 한번에 받아서 배열에 넣고, 또 다른 배열에 int값으로 바꾼 값 넣기
# A=[['홍길동',95],['이순신',77]]
# 성적 오름차순으로 정렬
# 이름만 출력
AA=[]
for i in range(int(input())):
    A=input().split()
    AA.append((A[0],int(A[1]))) # 배열 A[][] 공부하기 -> 튜플()이었음
AA=sorted(AA,key=lambda x:x[1])
for x in AA: # 이 for문이 뭘 위한건지 전혀 모르겠음
             # key값인 x가 AA 배열 안에 존재하는 만큼 for문을 iteration함
    print(x[0],end=' ')