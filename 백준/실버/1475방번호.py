import sys
input = sys.stdin.readline

N = input().strip()
N = [int(a) for a in str(N)]
# print(len(N))
result = 0
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

num1 = [0, 1, 2, 3, 4, 5, 7, 8]
num2 = [6, 9]

for n in num1:
    for i in range(len(N)):
        if N[i] == n:
            arr[n] += 1

x = 0

for i in range(len(N)):
    if N[i] in num2:
        x += 1
if x == 1 or x == 2:
    arr[9] = 1
elif x == 3 or x == 4:
    arr[9] = 2
elif x == 5 or x == 6:
    arr[9] = 3

# print(arr)
print(max(arr))
