# day는 날 수, a/b/c는 방문 주기이다.
a,b,c=map(int,input().split())
day=1
while True:
    if day%a==0 and day%b==0 and day%c==0:
        break
    else:
        day+=1
print(day)