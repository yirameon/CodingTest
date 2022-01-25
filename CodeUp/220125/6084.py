# h:1초에 몇번 확인하는가
# b:한 번 체크한 값을 저장할 때 사용하는 비트수
# c:좌우 등 소리를 저장할 트랙 개수(채널개수)
# s:녹음할 시간(초)
h,b,c,s=map(int,input().split())
result=round(h*b*c*s/8/1024/1024,1)
print(result,'MB')
