import sys
from collections import defaultdict

'''
defaultdict을 사용하여 시간 단축 key - age / value - num
한 번 반복문을 똘 때 합칠 수 있는 건 최대한 합침 (봄, 여름, 겨울)
'''

input = sys.stdin.readline

N, M, K = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
nutrient = [[5]*N for x in range(N)]
forest = [[defaultdict(lambda: 0) for _ in range(N)] for _ in range(N)]
dr, dc = (0, -1, -1, -1, 0, 1, 1, 1), (-1, -1, 0, 1, 1, 1, 0, -1)
answer = 0

for _ in range(M):
    r, c, age = map(int, input().split())
    forest[r-1][c-1][age] += 1
    answer += 1

# K년이 지날 때까지
for _ in range(K):
    # 모든 좌표에 대하여
    for r in range(N):
        for c in range(N):
            # Spring
            # (r, c)에 나무가 심겨져 있다면
            if forest[r][c]:
                new_trees = defaultdict(lambda: 0)
                dead_nutrient = 0
                for age, num in sorted(forest[r][c].items()):
                    # 여기서 전자가 더 많다면 min은 num -> 죽을 나무가 없다는 뜻
                    alive = min(nutrient[r][c] // age, num)
                    dead = num - alive
                    if alive > 0:
                        # 살아있는 나무가 있다면 영양소를 빼고 나이를 한 살 더 채워준다.
                        nutrient[r][c] -= age*alive
                        new_trees[age+1] = alive
                    # 죽은 나무는 dead_nutrient에 저장
                    dead_nutrient += (age//2)*dead
                    answer -= dead
                # forest를 update
                forest[r][c] = new_trees

                # Summer
                nutrient[r][c] += dead_nutrient

            # Winter
            nutrient[r][c] += A[r][c]
    # Fall
    for r in range(N):
        for c in range(N):
            trees = forest[r][c]
            if trees:
                for age, num in trees.items():
                    # 나이가 5로 나누어 떨어지는 나무들에 대하여
                    if age % 5 == 0:
                        # 확산
                        for i in range(8):
                            nr, nc = r+dr[i], c+dc[i]
                            if 0<=nr<N and 0<=nc<N:
                                forest[nr][nc][1] += num
                                answer += num

print(answer)