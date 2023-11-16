from collections import deque

n, m=map(int, input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]


result=1

def miro(x, y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
            return
    if graph[x][y]==1:
    # 지나갔으니까 0으로 변경
        graph[x][y]=0
        result=result+1
        for i in range(4):
            miro(x+dx[i], y+dy[i])
        
    else:
         return

miro(0,0)

print(result)