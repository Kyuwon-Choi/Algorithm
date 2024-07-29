import sys
from collections import deque
input = sys.stdin.readline

N, M, V= map(int, input().split())
# 그래프 행렬
graph = [[0]*(N+1) for _ in range(N+1)]
# 방문 리스트
dfs_visited=[0]*(N+1)
bfs_visited=[0]*(N+1)

for _ in range(M):
    u, v= map(int, input().split())
    graph[u][v] = graph[v][u] = 1

def dfs(V):
    dfs_visited[V]=1 #방문
    print(V, end=" ")
    for i in range(1, N+1):
        # 연결된 노드중 방문 기록이 없는 노드 찾기
        if graph[V][i] == 1 and dfs_visited[i] == 0:
            dfs(i)

def bfs(V):
    queue = deque([V])
    bfs_visited[V]=1
    while queue:
        V = queue.popleft()
        print(V, end=" ")
        for i in range(1, N+1):
            if graph[V][i] == 1 and bfs_visited[i] == 0:
                queue.append(i)
                bfs_visited[i]=1
dfs(V)
print()
bfs(V)