# 2022.01.21
# time.time()을 이용해서 수행시간 측정하기
# 선택 정렬 프로그램 코드 다시 보기
from random import randint
import time

# 배열에 10,000개의 정수를 삽입
array=[]
for _ in range(10000):
    array.append(randint(1,100)) # 1~100의 랜덤한 정수를 array에 넣기

# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택 정렬 프로그램
for i in range(len(array)):
    min_index=i     # 가장 작은 원소의 인덱스
    for j in range(i+1,len(array)):
        if array[min_index]>array[j]:
            min_index=j
    array[i],array[min_index]=array[min_index],array[i] # 스와프

end_time=time.time()
print('선택 정렬 성능 측정:',end_time-start_time) # 수행시간 출력

# 기본 정렬 라이브러리 성능 측정
start_time=time.time()

# 기본 정렬 라이브러리
array.sort()

end_time=time.time()
print('기본 정렬 라이브러리 성능 측정:',end_time-start_time)
