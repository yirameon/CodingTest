T=int(input())
for i in range(T):
    A,B=map(int, input().split())
    a,b=A,B
    while A!=0:
        B=B%A
        A,B=B,A
    GCD=B
    LCM=a*b//B
    print(LCM)

# 전혀 모르겠으니 유클리드 호제법과 최소공배수, 최대공약수 구하는거 벨로그에 포스팅할 것.