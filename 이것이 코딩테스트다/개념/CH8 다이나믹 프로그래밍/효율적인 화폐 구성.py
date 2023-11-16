N, M=map(int, input().split())
arr=[]

for i in range(N):
    arr.append(int(input()))

arr.sort()

result=0


start=0

while True:
    if start==M:
        break
    
    process=[]
    cycle=0

    for a in arr:
        if start+a<=M:
            process.append(start+a)
   
    
    if process==[]:
        result=-1
        break;
    start=max(process)
    result+=1

print(result)
