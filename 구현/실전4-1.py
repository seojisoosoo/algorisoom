import sys
input = sys.stdin.readline

n = input().strip()
start_g = n[0]
start_s = int(n[1])

garo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
sero = [1, 2, 3, 4, 5, 6, 7, 8]
num_g = 0  # 인덱스
num_s = 0


for i in range(8):
    if garo[i] == start_g:
        num_g = i
    if sero[i] == start_s:
        num_s = i

print(num_g, num_s)
result = 0  # 이동할 수 있는 경우의 수

if num_g+2 in range(8) and num_s-1 in range(8):
    result += 1
if num_g+2 in range(8) and num_s+1 in range(8):
    result += 1
if num_g+1 in range(8) and num_s+2 in range(8):
    result += 1
if num_g-1 in range(8) and num_s+2 in range(8):
    result += 1

print(result)
