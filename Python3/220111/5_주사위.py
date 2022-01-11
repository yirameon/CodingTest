A,B,C=map(int, input().split())
if A==B and B==C:
    money=10000+A*1000
elif (A==B and B!=C) or (A!=B and B==C) or (A==C and A!=B):
    if A==B:
        money=1000+A*100
    elif B==C:
        money=1000+B*100
    elif A==C:
        money=1000+C*100
elif A!=B and B!=C:
    L=[A,B,C]
    money=max(L)*100
print(money)