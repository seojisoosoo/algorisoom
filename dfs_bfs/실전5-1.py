import sys
from collections import deque, defaultdict

input = sys.stdin.readline

# 행렬 입력받기
N, M = map(int, input().split())
# 리스트 입력받기
arr = [list(input().strip()) for _ in range(N)]
graph = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        graph[i][j] = int(arr[i][j])

# dfs


def dfs(x, y):
    if x == -1 or x == N or y == -1 or y == M:
        return False
    if graph[x][y] == 0:
        graph[x][y] == 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return True


result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)
