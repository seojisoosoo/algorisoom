import sys
from collections import defaultdict
input = sys.stdin.readline

N, M, R = map(int, input().split())

visited = [False]*(N+1)
graph = defaultdict(set)
for i in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)

new = []
new.append(0)


def dfs(graph, start, visited):
    visited[start] = True
    new.append(start)
    for i in graph[start]:
        if not visited[int(i)]:
            dfs(graph, int(i), visited)


dfs(graph, R, visited)
if new[N-1] != N:
    new.append(0)
else:
    for i in range(N+1):
        if new[i] != i:
            new.insert(i, 0)

new = new[1:]
print(new)
