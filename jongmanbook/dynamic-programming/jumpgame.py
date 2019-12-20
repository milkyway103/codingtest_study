board = list()
def jumpgame(cx, cy):
    # 기저 사례 마지막 칸에 도착한 경우
    if cx == n-1 and cy == n-1:
        return True
    # 기저 사례 : 게임판 밖을 벗어난 경우
    if cx > n or cy > n:
        return False
    jumpSize = board[cx][cy]
    return jumpgame(cx + jumpSize, cy) or jumpgame(cx, cy + jumpSize)

cache = dict()
def jumpgame2(cx, cy):
    # 기저 사례 마지막 칸에 도착한 경우
    if cx == n-1 and cy == n-1:
        return True
    # 기저 사례 : 게임판 밖을 벗어난 경우
    if cx > n or cy > n:
        return False
    # 메모이제이션
    jumpSize = board[cx][cy]
    ret = cache.get((cx, cy), jumpgame(cx + jumpSize, cy) or jumpgame(cx, cy + jumpSize))
