N, M=map(int, input().split())
arr=list(map(int, input().split()))

rest=[]
max_rice=max(arr)
min_rice=min(arr)
result=min_rice

for rice in range(min_rice, max_rice+1):
    for a in arr:
        if a-rice>=0:
            rest.append(a-rice)
        else:
            rest.append(0)
    if sum(rest)<M:
        break;
    else:
        result=rice
    rest=[]

print(result)