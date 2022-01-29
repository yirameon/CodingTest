N,M=map(int,input().split())
A,B,d=map(int,input().split())
count=1
turn_time=0
Map=[]
been=[[0]*M for _ in range(M)]
for _ in range(N):
    Map.append(list(map(int,input().split())))
# 북동남서(0,1,2,3)
dA=[-1,0,1,0]
dB=[0,1,0,-1]
def turn_left():
    global d
    d-=1
    if d==-1:
        d=3
while True:
    turn_left()
    nA=A+dA[d]
    nB=B+dB[d]
    # 앞으로 갈 수 있으면 이동한다
    if been[nA][nB]==0 and Map[nA][nB]==0:
        been[nA][nB]=1
        A=nA
        B=nB
        count+=1
        continue
    else: # 앞으로 못가면 왼쪽으로 돈다
        turn_time+=1
    # 다 갔던 곳인지 확인하기
    if turn_time==4:
        nA=A-dA[d]
        nB=B-dB[d]
        # 뒤로 갈 수 있는지 확인하기
        if Map[nA][nB]==0:
            A=nA
            B=nB
        else:
            break
        turn_time=0
print(count)