N=int(input())
K=list(map(int, input().split()))

result=0

while True:
    if max(K)==0:
        break
    
    result+=max(K)
    if K.index(max(K))+1<len(K):
        K[K.index(max(K))+1]=0
    if K.index(max(K))-1>=-1:
        K[K.index(max(K))-1]=0
    K[K.index(max(K))]=0

print(result)