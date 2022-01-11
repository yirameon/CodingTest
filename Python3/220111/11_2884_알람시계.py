H,M=map(int,input().split())
print((H*60+M-45)//60%24,(M+60-45)%60)