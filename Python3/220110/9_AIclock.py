h,m,s=map(int,input().split())
D=h*3600+m*60+s+int(input())
print(D//3600%24,D//60%60,D%60)