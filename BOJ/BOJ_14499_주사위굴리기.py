from sys import stdin

# input
input = stdin.readline
N, M, x, y, K = list(map(int, input().split()))
maparr = [list(map(int, input().split())) for _ in range(N)]
dirarr = list(map(int, input().split()))

direction = [
    (2, 1, 5, 0, 4, 3), # east
    (3, 1, 0, 5, 4, 2), # west
    (4, 0, 2, 3, 5, 1), # north
    (1, 5, 2, 3, 0, 4) # south
]

# 동 서 북 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dice = [0]*6

for dir in dirarr:
    dir -= 1
    if not 0 <= x + dx[dir] < N or not 0 <= y + dy[dir] < M:
        continue
    x, y = x + dx[dir], y + dy[dir]
    temp = dice[:]
    for idx in range(6):
        dice[idx] = temp[direction[dir][idx]]
    if maparr[x][y] == 0:
        maparr[x][y] = dice[5]
    else:
        dice[5] = maparr[x][y]
        maparr[x][y] = 0
    print(dice[0])