from os import environ
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A, B, arrow = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


direction = [0, 1, 2, 3]  # 북동남서
environment = [0, 1]  # 육지 바다

result = 1  # 캐릭터가 방문한 칸의 수
map = arr[N][M]
new_direction = arrow
