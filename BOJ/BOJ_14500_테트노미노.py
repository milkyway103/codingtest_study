from sys import stdin

input = stdin.readline

N, M = list(map(int, input().split()))
maparr = [list(map(int, input().split())) for _ in range(N)]

# block 다시 만들기
block = [
    [(0, 0, 0, 0), (0, 1, 2, 3)],
    [(0, 1, 2, 3), (0, 0, 0, 0)],
    [(0, 0, 1, 1), (0, 1, 0, 1)],
    [(0, 1, 2, 2), (0, 0, 0, 1)],
    [(0, 1, 2, 2), (0, 0, 0, -1)],
    [(0, 0, 0, 1), (0, 1, 2, 0)],
    [(0, 0, 0, 1), (0, -1, -2, 0)],
    [(0, 0, 1, 2), (0, 1, 1, 1)],
    [(0, 0, 1, 2), (0, -1, -1, -1)],
    [(0, 0, 0, -1), (0, 1, 2, 2)],
    [(0, 0, 0, -1), (0, -1, -2, -2)],
    [(0, 1, 1, 2), (0, 0, 1, 1)],
    [(0, 1, 1, 2), (0, 0, -1, -1)],
    [(0, 0, 1, 1), (0, -1, -1, -2)],
    [(0, 0, 1, 1), (0, 1, 1, 2)],
    [(0, 0, 0, 1), (0, 1, 2, 1)],
    [(0, 1, 1, 2), (0, 0, -1, 0)],
    [(0, 1, 1, 1), (0, -1, 0, 1)],
    [(0, 0, 0, -1), (0, 1, 2, 1)]
]

x, y = 0, 0
answer = 0

for idx in range(N):
    for jdx in range(M):
        for kdx in block:
            s = maparr[idx][jdx]
            # xarr = [idx+_ for _ in kdx[0]]
            # yarr = [jdx+_ for _ in kdx[1]]
            try:
                for i in range(1, 4):
                    s+=maparr[idx+kdx[0][i]][jdx+kdx[1][i]]
                    # s+=maparr[xarr[i]][yarr[i]]
            except IndexError:
                continue
            answer = max(answer, s)
print(answer)