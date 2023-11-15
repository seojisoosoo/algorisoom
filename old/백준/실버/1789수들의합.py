import sys
input = sys.stdin.readline

s = int(input())

n = 0
num = 1  # 더해지는 숫자
result = num  # 더해가는 과정
while result < s or result == s:
    num += 1
    result += num
    n += 1


print(n)
