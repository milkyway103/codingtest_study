from sys import stdin
import copy

input = stdin.readline

N, M = list(map(int, input().split()))
maparr = [ list(map(int, input().split())) for _ in range(N)]

minans = float('inf')

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

U, R, D, L = 1, 2, 4, 8
dcctv = [[0],
         [U, R, D, L],
         [U|D, R|L],
         [U|R, R|D, D|L, L|U],
         [U|R|D, R|D|L, D|L|U, L|U|R],
         [U|R|D|L]]

cctvlist = [[maparr[idx][jdx], (idx, jdx)] for idx in range(N) for jdx in range(M) if maparr[idx][jdx] in [1,2,3,4,5]]
cctvnum = len(cctvlist)

def solution(depth):
    global minans, maparr, dx, dy
    # #의 개수를 세어서 minans랑 비교
    # 모든 cctv에 대해서 다 확인했다면
    if depth == cctvnum:
        temp = sum([ maparr[idx].count(0) for idx in range(N)])
        minans = min(minans, temp)
        return

    cctv, cdir = cctvlist[depth]
    for direction in dcctv[cctv]:
        temp = copy.deepcopy(maparr)
        for k in range(4):
            x, y = cdir[0], cdir[1]
            if direction & (1<<k):
                nx, ny = x, y
                while 0 <= nx < N and 0 <= ny < M and maparr[nx][ny] != 6:
                    maparr[nx][ny] = -1
                    nx, ny = nx + dx[k], ny + dy[k]
        # depth를 높여서 보내고
        solution(depth + 1)
        # 되돌린다. (백트래킹)
        maparr = copy.deepcopy(temp)

solution(0)
print(minans)