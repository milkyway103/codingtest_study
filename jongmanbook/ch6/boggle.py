from sys import stdin
'''
보글 게임판의 (y, x)에서 시작하는 단어 word의 존재 여부를 반환
'''
input = stdin.readline
n = int(input())
boggle = [list(map(int, input().split())) for _ in n]

dx = (-1, -1, -1, 1, 1, 1, 0, 0)
dy = (-1, 0, 1, -1, 0, 1, -1, 1)


def inrange(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return False
    return True


def hasword(y, x, word):
    if not inrange(y, x):
        return False
    if boggle[y][x] != word[0]:
        return False
    if len(word) == 1:
        return True
    for idx in range(8):
        ny = y+dy[idx]
        nx = x+dx[idx]
        if hasword(ny, nx, word[1:]):
            return True
