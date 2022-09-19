import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort()
# weight = []

# for i in range(len(arr)):
#     weight.append(arr[i]*(n-i))

# weight.sort(reverse=True)
# print(weight[0])

max_weight = 0

for i in range(len(arr)):
    if arr[i]*(n-i) > max_weight:
        max_weight = arr[i]*(n-i)

print(max_weight)
