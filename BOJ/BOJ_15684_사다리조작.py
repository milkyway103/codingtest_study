from sys import stdin

input = stdin.readline

n, m, h = list(map(int, input().split()))
arr = [ [0]*(n) for _ in range(h)]
answer = 4
for _ in range(m):
    x, y = list(map(int, input().split()))
    arr[x-1][y-1] = 1

def backtracking(cnt, x, y):
    global answer
    if answer <= cnt:
        return
    if travle():
        answer = min(answer, cnt)
        return
    if cnt == 3:
        return
    # h는 세로선마다 가로줄을 놓을 수 있는 횟수라고 되어있지만
    # 사실상 height
    for idx in range(x, h):
        k = y if idx == x else 0
        for jdx in range(k, n-1):
            if arr[idx][jdx]:
                jdx += 1
                continue
            if jdx < n - 1 and arr[idx][jdx + 1]:
                jdx += 2
                continue
            else:
                arr[idx][jdx] = 1
                backtracking(cnt+1, idx, jdx+2)
                arr[idx][jdx] = 0
    return

def travle():
    for idx in range(n):
        y = idx
        x = 0
        while x<h:
            if arr[x][y] == 1:
                y += 1
            elif y > 0 and arr[x][y-1]:
                y -= 1
            x += 1
        if y != idx:
            return False
    return True

backtracking(0, 0, 0)

if answer == 4:
    answer = -1
print(answer)