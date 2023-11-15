from collections import deque
import queue
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(input().strip()))

for i in range(N):
    for j in range(M):
        graph[i][j] = int(graph[i][j])

# print(N, M, graph)


def dfs(x, y):
    result = 0
    if x == -1 or x == N or y == -1 or y == M:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        result += 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
    return result


# result = 0

for i in range(N):
    for j in range(M):
        # if dfs(i, j):
        #     result += 1
        result = dfs(i, j)

print(result)

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]


# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if nx < 0 or ny < 0 or nx >= N or ny >= M:
#                 continue
#             if graph[nx][ny] == 0:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y]+1
#                 queue.append((nx, ny))
#     return graph[N-1][M-1]


# print(bfs(0, 0))

# 이게 x왼오, y왼오로 해서 - 1, 1, 0, 0 / 0, 0, -1, 1로 표현한 듯...
