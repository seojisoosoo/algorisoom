import sys
input = sys.stdin.readline

N = int(input())
arr = list(input().strip().split(' '))

print(N, arr)

i = 1  # 행
j = 1  # 열
for a in range(len(arr)):
    if arr[a] == 'L':
        i -= 1
        if 1 <= i <= N:
            i = i
        else:
            i += 1
    elif arr[a] == 'R':
        i += 1
        if 1 <= i <= N:
            i = i
        else:
            i -= 1
    elif arr[a] == 'U':
        j -= 1
        if 1 <= j <= N:
            j = j
        else:
            j += 1
    elif arr[a] == 'D':
        j += 1
        if 1 <= j <= N:
            j = j
        else:
            j -= 1

    print(j, i)
