n, m=map(int, input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def drink(x, y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    
    if graph[x][y]==0:
        # 더 나아가야하는 경우임!
        # 방문하니까 방문처리하기
        graph[x][y]=1
        for i in range(4):
            drink(x+dx[i], y+dy[i])
        return True;
    
    else:
        return False

result=0;

for i in range(n):
    for j in range(m):
        if graph[i][j]==True:
            result+=1

print(result)