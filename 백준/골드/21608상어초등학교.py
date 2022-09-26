import collections
import sys
input = sys.stdin.readline

dic = collections.defaultdict(list)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N**2)]

for i in range(N**2):
    dic[arr[i][0]].append(arr[i][1:5])

# print(dic)
