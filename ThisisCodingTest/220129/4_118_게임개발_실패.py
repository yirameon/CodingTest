N,M=map(int,input().split())
A,B,direction=map(int,input().split())
# 방문한 위치를 저장할 배열 선언
d=[[0]*M for _ in range(N)]
Map=[]
for i in range(N):
    Map.append(list(map(int,input().split())))
d[A][B]=1
# 방향 정의, 북동남서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction-=1
    if direction==-1:
        direction=3

count=1
turn_time=0

while True:
    turn_left()
    nx=A+dx[direction]
    ny=B+dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny]==0 and Map[nx][ny]==0:
        d[nx][ny]=1
        A=nx
        B=ny
        count+=1
        turn_time=0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time+=1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time==4:
        nx=A-dx[direction]
        ny=B-dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if Map[nx][ny]==0:
            A=nx
            B=ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time=0
print(count)