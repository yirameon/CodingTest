for i in range(int(input())):
    max=0
    for i in range(int(input())):
        price,name=input().split()
        price=int(price)
        if price>max:
            max=price
            mName=name
    print(mName)
