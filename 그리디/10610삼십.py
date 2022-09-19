import sys
input = sys.stdin.readline

n = list((input().strip()))
len_n = len(n)
for i in range(len_n):  # 자연수 리스트로 바꿔주는 과정
    n[i] = int(n[i])

n.sort(reverse=True)
sum = 0
for i in range(len_n):
    sum += n[i]
    # print(sum)

zero = 0
for j in range(len_n):
    if n[i] == 0:
        zero += 1
# print(n)


if sum % 3 == 0 and zero > 0:  # 3의 배수인 경우
    for q in range(len_n):
        print(n[q], end='')
    print("\n")

else:
    print(-1)
