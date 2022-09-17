n = 5
m = 8  # m번 더하기
k = 3  # k번 연속 x

array = [2, 3, 5, 4, 6]

for i in range(n):
    for j in range(n-i-1):
        if (array[j] < array[j+1]):
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp

result = 0  # 결과값
num = 0  # 더한 횟수
index = 0  # 인덱스

for i in range(m):
    if num < k:
        result += array[index]
        num += 1
    else:
        result += array[index+1]
        num = 0
print(result)
