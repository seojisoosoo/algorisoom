N, K = map(int, input().split())

result = 0  # 수행한 횟수

while N != 1:
    if N % K == 0:
        N /= K
    else:
        N -= 1
    result += 1

print(result)
