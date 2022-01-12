dish_list=list(str(input()))
for i in range(len(dish_list)):
    if i==0:
        h=10
    elif dish_list[i]==dish_list[i-1]:
        h=h+5
    elif dish_list[i]!=dish_list[i-1]:
        h=h+10
print(h)
