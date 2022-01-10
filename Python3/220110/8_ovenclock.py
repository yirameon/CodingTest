A,B = map(int, input().split())
C = int(input())

if B+C < 60:
    print("%d %d" %(A,B+C))
elif B+C >= 60:
    hour = (B+C)//60
    minute = (B+C)%60
    if A+hour < 24:
        print("%d %d" %(A+hour, minute))
    elif A+hour >= 24:
        print("%d %d" %(A+hour-24, minute))
else:
    print("")