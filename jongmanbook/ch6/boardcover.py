from sys import stdin
import copy

input = stdin.readline

# 주어진 칸을 덮을 수 있는 네 가지 방법
# 블록을 구성하는 세 칸의 상대적 위치 (dy, dx)의 목록

covertype = (
    ((0, 0), (1, 0), (0, 1)),
    ((0, 0), (0, 1), (1, 1)),
    ((0, 0), (1, 0), (1, 1)),
    ((0, 0), (1, 0), (1, -1))
)

# board의 (y, x)를 type번 방법으로 덮거나, 덮었던 블록을 없앤다.
# delta = 1이면 덮고, -1이면 덮었던 블록을 없앤다.
# 만약 블록이 제대로 덮이지 않은 경우 (게임판 밖으로 나가거나,
# 겹치거나, 검은 캄을 덮을 때) False를 반환한다.

def set(board, y, x, type, delta):
    ok = True
    for idx in range(3):
        ny = y + covertype[type][idx][0]
        nx = x + covertype[type][idx][1]
        if (ny<0 or ny>=len(board) or nx<0 or nx>=len(board[0])):
            ok = False
        else:
            board[ny][nx] += delta
            if (board[ny][nx]) > 1:
                ok = False
    return ok

'''
board의 모든 빈 칸을 덮을 수 있는 방법의 수를 반환한다.
board[idx][jdx] = 1 이미 덮인 칸 혹은 검은 칸
board[idx][jdx] = 0 아직 덮이지 않은 칸
'''
def cover(board):
    y, x = -1, -1
    for idx in range(len(board)):
        for jdx in range(len(board[0])):
            if board[idx][jdx] == 0:
                y, x = idx, jdx
                break
        if y!=-1:
            break
    # 기저 사례 : 모든 칸을 채웠으면 1을 반환한다.
    if y==-1:
        return 1
    ret = 0
    for type in range(4):
        # 만약 board[y][x]를 type형태로 덮을 수 있으면 재귀 호출
        if set(board, y, x, type, 1):
            ret += cover(board)
        # 덮었던 블록을 치운다.
        set(board, y, x, type, -1)
    return ret

def inputfunc():
    C = int(input())
    boardlist = list()
    for TC in range(C):
        H, W = list(map(int, input().split()))
        board = list()
        temp_board = [input() for _ in range(H)]
        for idx in range(H):
            temp = list()
            for jdx in range(W):
                if temp_board[idx][jdx] == '#':
                    temp.append(1)
                else:
                    temp.append(0)
            board.append(temp)
        boardlist.append(board)
    return C, boardlist

def solve():
    C, boardlist = inputfunc()
    for TC in range(C):
        board = copy.deepcopy(boardlist[TC])
        check = len(board)*len(board[0]) - sum([sum(board[idx]) for idx in range(len(board))])
        if (check%3) != 0:
            print(0)
        else:
            print(cover(board))

solve()