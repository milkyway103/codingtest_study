from sys import stdin

input = stdin.readline

N, M = list(map(int, input().split()))
labarr = [list(map(int, input().split())) for _ in range(N)]
c = [[False]*M for _ in range(N)]
# 벽 더할 것을 감안하여 safe의 초기값은 -3
safe, v, virus = -3, list(), 100
answer = 0

# 안전한 위치를 세고, 바이러스의 위치를 저장
for idx in range(N):
    for jdx in range(M):
        if labarr[idx][jdx] != 1:
            safe += 1
        if labarr[idx][jdx] == 2:
            v.append((idx, jdx))

def expand(x, y):
    res = 1
    c[x][y] = True
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<M:
            # 만약 아직 감염되지 않았고, 0이라면
            if not (c[nx][ny] or labarr[nx][ny]):
                res += expand(nx, ny)
    return res

# 1(벽)을 세 개 추가할 수 있음
# 2는 상 / 하 / 좌 / 우로 이동하면서 0이면 2로 변환시키고 1이면 거기서 멈춘다.

def solution(wall, x, y):
    global virus, c
    if wall == 3:
        cnt = 0
        c = [[False]*M for _ in range(N)]
        for idx, jdx in v:
            cnt += expand(idx, jdx)
        virus = mBin(virus, cnt)
        return
    for idx in range(x, N):
        k = y if idx == x else 0
        for jdx in range(k, M):
            if labarr[idx][jdx] == 0:
                labarr[idx][jdx] = 1
                solution(wall+1, idx, jdx+1)
                labarr[idx][jdx] = 0

solution(0, 0, 0)
print(safe - virus)