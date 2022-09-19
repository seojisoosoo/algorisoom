import sys
input = sys.stdin.readline

A, B = map(int, input().split())

result = 0

while True:
    if B % 2 == 0:
        B = B // 2
    else:
        if B % 10 == 1:
            B = B//10
        else:
            result = -1
            break
    result += 1
    if B == A:
        result += 1
        break
    if B < A:
        result = -1
        break
print(result)
