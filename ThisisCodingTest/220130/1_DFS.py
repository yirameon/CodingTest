# DFS 예제(p.142)
# DFS 메서드 정의
def dfs(graph,v,visited):
    # 현재 노드를 방문 처리
    visited[v]=True
    print(v,end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph=[
    [],         # 0번 노드는 연결되어있는 노드가 없음
    [2,3,8],    # 1번 노드는 2번,3번,8번 노드와 연결되어있음
    [1,7],      # 2번 노드는 1번, 7번 노드와 연결되어있음
    [1,4,5],    # ...
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited=[False]*9

# 정의된 DFS 함수 호출
dfs(graph,1,visited) # 1은 시작노드를 뜻함
