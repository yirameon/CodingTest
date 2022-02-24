skh=list(map(int,input().split()))
if sum(skh)>=100:
    print('OK')
else:
    num_index=skh.index(min(skh))
    if num_index==0:
        print('Soongsil')
    elif num_index==1:
        print('Korea')
    else:
        print('Hanyang')
