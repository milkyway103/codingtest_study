def solution(n, build_frame):
    answer = list()

    dx = (1, 1, 1, -1, -1, -1, 0, 0)
    dy = (0, 1, -1, 0, 1, -1, 1, -1)

    arr = [[[False, False] for _ in range(n + 1)] for _ in range(n+1)]

    for frame in build_frame:
        x, y, a, b = frame
        if b == 0:
            arr[x][y][a] = False
            if not erase(n, arr):
                arr[x][y][a] = True
        else:
            if ispossible(x, y, a, arr):
                arr[x][y][a] = True
    for x in range(n+1):
        for y in range(n+1):
            if arr[x][y][0]:
                answer.append([x, y, 0])
            if arr[x][y][1]:
                answer.append([x, y, 1])
    print(answer)
    return answer

def erase(n, arr):
    for x in range(n+1):
        for y in range(n+1):
            for k in range(2):
                if arr[x][y][k] and not ispossible(x, y, k, arr):
                    return False
    return True

def ispossible(x, y, a, arr):
    global n
    if a == 0:
        if y == 0 \
        or arr[x][y][1] \
        or ( y-1 >= 0 and arr[x][y-1][0]) \
        or ( x-1 >= 0 and arr[x-1][y][1]):
            return True
    else:
        if (y-1 >= 0 and arr[x][y-1][0]) \
        or (x+1 >= 0 and arr[x+1][y-1][0]) \
        or (arr[x+1][y][1] and arr[x-1][y][1]):
            return True
    return False
