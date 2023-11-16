from collections import deque

n, m=map(int, input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def miro(x,y):
    queue=deque()
    queue.append(x, y)

    while queue:
        queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

        if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
            continue
        
        if graph[nx][ny]==0:
            continue
        if graph[nx][ny]==1:
            # 갈 수 있는 길인 경우
            graph[nx][ny]=graph[x][y]+1
            queue.append((nx, ny))

    return graph[n-1][m-1]

print(miro(0,0))