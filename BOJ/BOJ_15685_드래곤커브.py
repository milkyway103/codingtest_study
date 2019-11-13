from sys import stdin

# v는 10세대까지 방향을 미리 저장해놓을 배열
v, ans = [0], 0
arr = [[0]*101 for _ in range(101)]
dx, dy = (1, 0, -1, 0), (0, -1 ,0, 1)

for idx in range(1, 11):
    # k는 1, 2, 4, ...
    k = 1<<(idx-1)
    # 거슬러 올라가면서 방향을 +1 (90도 회전)
    for jdx in range(k):
        v.append((v[k-jdx-1]+1)%4)

# 좌표공간상에 표현
for _ in range(int(input())):
    x, y, d, g = map(int, input().split())
    arr[x][y] = 1
    # 세대에 맞게
    for i in range(1<<g):
        # 입력받은 d를 기존에 만들어둔 v배열에 더해가면서 좌표공간상에 표현
        x, y = x+dx[(v[i]+d)%4], y+dy[(v[i]+d)%4]
        arr[x][y] = 1

# ans 계산
for idx in range(100):
    for jdx in range(100):
        if arr[idx][jdx] and arr[idx+1][jdx] and arr[idx][jdx+1] and arr[idx+1][jdx+1]:
            ans += 1

print(ans)