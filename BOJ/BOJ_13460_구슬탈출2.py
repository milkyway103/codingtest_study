from sys import stdin
from collections import deque

input = stdin.readline
n, m = map(int, input().split())
a = [list(input().strip()) for _ in range(n)]
# print(a)
# to check visited path
check = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
# to check up, right, down, left
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
q = deque()

def init():
    # location of red, blue initialization
    _rx, _ry, _bx, _by = [0]*4
    for idx in range(n):
        for jdx in range(m):
            if a[idx][jdx] == 'R':
                _rx, _ry = idx, jdx
            elif a[idx][jdx] == 'B':
                _bx, _by = idx, jdx
    # append location of red, blue and count(initialized 0)
    q.append((_rx, _ry, _bx, _by, 0))
    # print((_rx, _ry, _bx, _by, 0))
    check[_rx][_ry][_bx][_by] = True

def move(_x, _y, dx, dy, _c):
    while a[_x+dx][_y+dy] != '#' and a[_x][_y] != 'O':
        _x += dx
        _y += dy
        # _c for move count
        # if location of red, blue is same, c를 활용하여 옮길 공을 판별
        _c += 1
    return _x, _y, _c

def bts():
    while q:
        # print(q)
        rx, ry, bx, by, d = q.popleft()
        # if move count is over 10, break
        if d>= 10:
            break
        # searching for four direction
        for idx in range(4):
            nrx, nry, rc = move(rx, ry, dx[idx], dy[idx], 0)
            # print('r',nrx, nry, rc, 'idx :', idx)
            nbx, nby, bc = move(bx, by, dx[idx], dy[idx], 0)
            # print('b',nbx, nby, bc)
            # if blue is in '0', continue
            if a[nbx][nby] == 'O':
                continue
            if a[nrx][nry] == 'O':
                print(d+1)
                return
            if nrx == nbx and nry == nby:
                # what color is moved using c
                if rc > bc:
                    nrx, nry = nrx - dx[idx], nry - dy[idx]
                else:
                    nbx, nby = nbx - dx[idx], nby - dy[idx]
                # bts
                # if nrx, nry, nbx, nby path is not checked, check and append
            if not check[nrx][nry][nbx][nby]:
                check[nrx][nry][nbx][nby] = True
                # print((nrx, nry, nbx, nby, d+1))
                q.append((nrx, nry, nbx, nby, d+1))
    print(-1)
init()
bts()