import sys

input = sys.stdin.readline

R, C = map(int, input().split())
graph = []
for i in range(R):
    li = list(map(str, input().strip()))
    graph.append(li)

def dfs(x, y, visited):
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    max_path = 0

    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:
            char_index = ord(graph[nx][ny]) - ord('A')
            if not visited[char_index]:
                visited[char_index] = True
                max_path = max(max_path, dfs(nx, ny, visited) + 1)
                visited[char_index] = False

    return max_path

visited = [False] * 26 
visited[ord(graph[0][0]) - ord('A')] = True
print(dfs(0, 0, visited) + 1)
