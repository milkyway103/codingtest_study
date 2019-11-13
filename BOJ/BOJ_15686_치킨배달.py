from sys import stdin
from itertools import combinations

input = stdin.readline
n, m = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 3000
chickens = list()
houses = list()
for idx in range(n):
    for jdx in range(n):
        if arr[idx][jdx] == 2:
            chickens.append((idx, jdx))
        elif arr[idx][jdx] == 1:
            houses.append((idx, jdx))

# 치킨집의 조합에 대하여 도시 최소 치킨 거리 구하기
for chi in combinations(chickens, m):
    result = 0
    for hx, hy in houses:
        # 집을 기준으로 최소 치킨 거리 구해서
        result += min([abs(cx-hx)+abs(cy-hy) for cx, cy in chi])
    # update ans
    ans = min(ans, result)
print(ans)