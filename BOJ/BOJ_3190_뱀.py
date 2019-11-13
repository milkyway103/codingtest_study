from sys import stdin

# input
input = stdin.readline
N = int(input())
board = [[2]+[0 for _ in range(N)]+[2] for _ in range(N)]
board.insert(0, [2 for _ in range(N+2)])
board.append([2 for _ in range(N+2)])
K = int(input())
for idx in range(K):
    x, y = list(map(int, input().split()))
    board[x][y] = 1
L = int(input())
dirarr = list()
for idx in range(L):
    x, dir = list(input().split())
    if dir=='L':
        dir = -1
    else:
        dir = 1
    dirarr.append([int(x), dir])

# up right down left
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def outboundary(x, y):
    if not 0<=x<N:
        return True
    if not 0<=y<N:
        return True
    return False

def turn(dir, turndir):
    dir = dir+turndir
    if dir > 3:
        dir = 0
    if dir < 0:
        dir = 3
    return dir

def move():
    # initial loc of snake
    snake = [(1, 1)]
    # initial dir of snake
    dir = 1
    count = 0
    while True:
        count += 1
        # thisloc
        _x, _y = snake[-1][0] + dx[dir], snake[-1][1] + dy[dir]
        # print(count, dir,':', _x, _y)
        # 만약 뱀의 다음 위치가 snake list에 있거나 out of boundary라면 return
        if (_x, _y) in snake or board[_x][_y] == 2:
            print(count)
            return
        # 사과가 있으면 지금 위치만을 append한다.
        if board[_x][_y] == 1:
            board[_x][_y] = 0
            snake.append((_x, _y))
            # print(snake)
            # 사과가 없으면 지금 위치를 append하고 처음 위치를 pop한다 (뱀의 길이는 그대로)
        else:
            snake.append((_x, _y))
            snake.pop(0)
            # print(snake)
        # 만약 이동해야 할 타이밍이라면 dir을 바꾼다.
        if dirarr != [] and count == dirarr[0][0]:
            dir = turn(dir, dirarr[0][1])
            dirarr.pop(0)

move()







