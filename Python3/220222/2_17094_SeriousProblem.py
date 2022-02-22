len_s=int(input())
S=list(input())
num_2=S.count('2')
num_e=S.count('e')
if num_2>num_e:
    print('2')
elif num_2<num_e:
    print('e')
else:
    print('yee')
