from sys import stdin
import copy
from collections import deque

input = stdin.readline
n = int(input())
# 입력받은 값들을 저장한 board
board = [list(map(int, input().split())) for _ in range(n)]
# print(board)
ans, queue = 0, deque()

def get(idx, jdx):
    if board[idx][jdx]:
        queue.append(board[idx][jdx])
        board[idx][jdx] = 0

def merge(idx, jdx, di, dj):
    while queue:
        x = queue.popleft()
        # 이 행 또는 열에 이미 저장된 숫자가 없으면 저장
        if not board[idx][jdx]:
            board[idx][jdx] = x
        # 같은 숫자이면 합치고 뒤로 이동
        elif board[idx][jdx] == x:
            board[idx][jdx] = x*2
            idx, jdx = idx+di, jdx+dj
        # 다른 숫자이면 뒤로 이동해서 저장
        else:
            idx, jdx = idx+di, jdx+dj
            board[idx][jdx] = x

def move(k):
    if k == 0: # up
        for jdx in range(n):
            for idx in range(n):
                # idx행의 모든 숫자를 queue에 push
                get(idx, jdx)
            # queue에 들어간 숫자를 대상으로 jdx 열에서 merge
            merge(0, jdx, 1, 0)
    elif k == 1: # down
        for jdx in range(n):
            # idx행에 대해 거꾸로 queue에 push
            for idx in range(n-1, -1, -1):
                get(idx, jdx)
            # queue에 들어간 숫자를 대상으로 jdx 열에서 merge
            merge(n-1, jdx, -1, 0)
    elif k == 2: # left
        for idx in range(n):
            # jdx열에 대해 queue에 push
            for jdx in range(n):
                get(idx, jdx)
            # queue에 들어간 숫자를 대상으로 idx 행에서 merge
            merge(idx, 0, 0, 1)
    else: # right
        for idx in range(n):
            # jdx열에 대해 거꾸로 queue에 push
            for jdx in range(n-1, -1, -1):
                get(idx, jdx)
            # queue에 들어간 숫자를 대상으로 jdx열에서 merge
            merge(idx, n-1, 0, -1)

def solve(cnt):
    global board, ans
    if cnt == 5:
        for idx in range(n):
            ans = max(ans, max(board[idx]))
        return
    b = copy.deepcopy(board)
    for k in range(4):
        move(k)
        solve(cnt+1)
        board = copy.deepcopy(b)

solve(0)
print(ans)


