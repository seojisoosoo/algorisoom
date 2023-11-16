X=int(input())

start=1
result=0

while True:
    if start==X:
        break

    process=[]
    if start*5<=X:
        process.append(start*5)
    if start*3<=X:
        process.append(start*3)
    if start*2<=X:
        process.append(start*2)
    if start+1<=X:
        process.append(start+1)
    start=max(process)
    result+=1

print(result)
