N, M=map(int, input().split())

arr=[]

for i in range(N):
    arr.append(list(map(int, input().split())))
    
min_list=[]
for i in range(N):
    min_list.append(min(arr[i]))

answer=max(min_list)

print(answer)


