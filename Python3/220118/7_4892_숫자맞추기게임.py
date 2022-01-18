i=1
while True:
    N0=int(input())
    if N0==0:
        break
    N1=3*N0
    if N1%2==0:
        N2=N1//2
        result='even'
    elif N1%2!=0:
        N2=(N1+1)/2
        result='odd'
    N3=3*N2
    N4=N3//9
    print('%d. '%i+result+' %d'%N4)
    i+=1
