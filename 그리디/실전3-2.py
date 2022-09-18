N, M = map(int, input().split())  # 행

arr = [[*map(int, input().split())] for _ in range(N)]
card = []

for i in range(N):
    card.append(min(arr[i]))

max_num = max(card)

print(max_num)
