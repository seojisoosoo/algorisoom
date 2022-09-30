import sys
from collections import deque, defaultdict

input = sys.stdin.readline
num = int(input())  # 컴퓨터의 수
link = int(input())
dic = defaultdict(set)

for i in range(link):
    a, b = map(int, input().split())
    dic[a].add(b)
    dic[b].add(a)

virus = 0

visited = [False]*(num+1)


def bfs(dic, start, visited, virus):
    queue = deque([start])

    while queue:
        j = queue.popleft()
        for i in dic[j]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                virus += 1
    return virus


print(bfs(dic, 1, visited, virus)-1)
