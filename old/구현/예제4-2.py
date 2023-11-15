import sys
input = sys.stdin.readline

N = int(input())
print(N)

m = 60
s = 60
time = [N, m, s]  # 시, 분, 초
result = 0  # 3이 하나라도 포함되는 경우

for i in range(N+1):
    for j in range(m):
        for k in range(s):
            if i % 10 == 3 or j//10 == 3 or j % 10 == 3 or k//10 == 3 or k % 10 == 3:
                result += 1

print(result)

# or 연산자를 썼는데, 그냥 if '3' in str(i) + str(j) + str(k) 이렇게 쓰면 훨 쉽다!
