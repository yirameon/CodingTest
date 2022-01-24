A=[input() for i in range(6)]
num=A.count('W')
if num>=5:
    print(1)
elif 2<num<5:
    print(2)
elif 0<num<3:
    print(3)
else:
    print(-1)
