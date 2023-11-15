# 크기가 N, 모든 값이 0안 1차원 리스트 만들기
N=10
a=[0]*N

# 리스트 컴프리헨션
# 0~19 숫자 중에서 홀수만 포함하는 경우
array=[i for i in range(20) if i%2==1]

# N*M크기의 2차원 리스트 초기화
n=3
m=4
array=[[0]*m for _ in range(n)]
# => [[0,0,0,0], [0,0,0,0], [0,0,0,0]]

# 내림차순 정렬
a.sort(reverse=True)

