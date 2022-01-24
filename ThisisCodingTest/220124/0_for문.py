numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
# 100이상의 숫자만 출력하기
for i in numbers:
    if i>=100:
        print(i)
i=0
# print(i for i in numbers if i>=100)

# 홀짝 구분하기
for i in numbers:
    if i%2==0:
        print('{}는 짝수입니다'.format(i))
    elif i%2!=0:
        print('{}는 홀수입니다'.format(i))
    
# 자릿수 확인하기
for i in numbers:
    print('{}는 {}자릿수입니다'.format(i,len(str(i))))

# 숫자 하나씩 출력하기
list_of_list = [[1,2,3], [4,5,6,7], [8,9]]
for i in list_of_list:
    for j in i:
        print(j)

# output=[[1,4,7],[2,5,8],[3,6,9]]
A=[1,2,3,4,5,6,7,8,9]
output=[[],[],[]]
for i in A:
    output[(i+2)%3].append(i) # output 0((i-1)%3)번째 요소에 1(i)을 넣기
print(output)