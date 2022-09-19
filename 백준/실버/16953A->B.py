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

# 뒷 숫자가 1이 아닌(3,5,7,9와 같은) 홀수가 오는 경우도 생각해야한다.
# 모든 경우의 수를 판단할 것!
