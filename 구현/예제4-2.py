import sys
input = sys.stdin.readline

N = int(input())
print(N)

m = 60
s = 60
time = [N, m, s]  # 시, 분, 초
result = 0  # 3이 하나라도 포함되는 경우

# 아직 푸는중!!!
for i in range(N+1):
    for j in range(m+1):
        for k in range(s+1):
            if i % 10 == 3 or j//10 == 3 or j % 10 == 3 or k//10 == 3 or k % 10 == 3:
                result += 1

print(result)
