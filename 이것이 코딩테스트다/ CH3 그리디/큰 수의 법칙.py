# M번 더하여 가장 큰 수 만들기 -> 같은 수는 연속으로 K번 초과할 수 없음

N, M, K=map(int, input().split())
array=list(map(int, input().split()))

array.sort() # 순서대로 정렬
# print(array)

first=array[-1]
second=array[-2]

flag=0
answer=0
for i in range(M):
    if flag!=K:
        answer+=first
        flag+=1
    else:
        answer+=second
        flag=0
    
print(answer)