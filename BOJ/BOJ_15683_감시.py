from sys import stdin
import copy

input = stdin.readline

N, M = list(map(int, input().split()))
maparr = [ list(map(int, input().split())) for _ in range(N)]

minans = float('inf')

# 각 cctv가 감시할 수 있는 영역을 check하기 위한 array
dcctv = [
    # 1 -> 4개의 경우의 수
    [[(1, 0)], [(0, 1)], [(-1, 0)], [(0, -1)]],
    # 2 -> 2개의 경우의 수
    [[(1, 0), (-1, 0)], [(0, 1), (0, -1)]],
    # 3 -> 4개의 경우의 수
    [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
    # 4 -> 4개의 경우의 수
    [[(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)], [(0, -1), (-1, 0), (0, 1)]],
    # 5 -> 1개의 경우의 수
    [[(-1, 0), (1, 0), (0, -1), (0, 1)]]
]

cctvlist = [[maparr[idx][jdx], (idx, jdx)] for idx in range(N) for jdx in range(M) if maparr[idx][jdx] in [1,2,3,4,5]]
wallnum = sum([maparr[idx].count(6) for idx in range(N)])
cctvnum = len(cctvlist)
barr = [[0]*M for idx in range(N)]

def solution(depth):
    global minans, maparr, barr
    # #의 개수를 세어서 maxans랑 비교
    # 모든 cctv에 대해서 다 확인했다면
    if depth == cctvnum:
        temp = sum([ barr[idx].count(0) for idx in range(N)])
        minans = min(minans, temp)
        return

    cctv, cdir = cctvlist[depth]
    for direction in dcctv[cctv-1]:
        # 모든 가능한 경우의 수에 대해
        for dx, dy in direction:
            x, y = cdir[0], cdir[1]
            while 0<=x<N and 0<=y<M and maparr[x][y] != 6:
                barr[x][y] += 1
                x, y = x + dx, y + dy
        # depth를 높여서 보내고
        solution(depth+1)
        # 되돌린다. (백트래킹)
        for dx, dy in direction:
            x, y = cdir[0], cdir[1]
            while 0 <= x < N and 0 <= y < M and maparr[x][y] != 6:
                barr[x][y] -= 1
                x, y = x + dx, y + dy

solution(0)
print(minans-wallnum)