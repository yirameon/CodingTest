# 이미지의 가로 해상도 w, 세로 해상도 h, 한 픽셀을 저장하기 위한 비트 b
w,h,b=map(int,input().split())
result=w*h*b/8/1024/1024
print('{:.2f}'.format(result),'MB')