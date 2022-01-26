N=int(input())
A=N
input=0
result=0
i=0
input_list=[0 for i in range(2)]
sum_list=[0 for i in range(2)]
while True:
    input_raw=A
    if input_raw<10: # 받은 input이 한자리수일때
        input_list[0]=0
        input_list[1]=input_raw
    else: # 받은 input이 두자리수일때
        input_list=list(map(int,str(input_raw)))
    sum_input=sum(input_list) # 받은 input의 두자리수 합 구하기
    if sum_input<10: # 두 자리수 합이 한자리수일때
        sum_list[0]=0
        sum_list[1]=sum_input
    else: # 두 자리수 합이 두자리수일때
        sum_list=list(map(int,str(sum_input)))
    result=input_list[1]*10+sum_list[1]
    A=result
    i+=1
    # print(result)
    if result==N:
        break
print(i)