while 1:
  A,B=map(int,input().split())
  if A==0 and B==0:
    break
  elif A%B==0:
    print('multiple')
  elif B%A==0:
    print('factor')
  elif A!=0 and B!=0 and A%B!=0 and B%A!=0:
    print('neither')
