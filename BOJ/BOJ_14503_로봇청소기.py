from sys import stdin

input = stdin.readline
N, M = list(map(int, input().split()))
r, c, d = list(map(int, input().split()))
statearr = [ list(map(int, input().split())) for _ in range(N)]
# 청소한 구역을 check하는 array
check = [ [False]*M for _ in range(N)]

# 로봇청소기는 처음에는 (default 0) 북쪽을 바라보고 있으면서
# 왼쪽으로 회전하기 때문에 다음과 같은 순서로 darr를 저장해준다.
# 0:북 1:동 2:남 3:서
darr = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def solution(x, y, d):
    check[x][y] = True
    # 모든 방향에 대해
    for _ in range(4):
        d = (d+3) % 4
        # 1) 벽이 없고 (not statearr[x+darr[d][0][y+darr[d][1])
        # 2) 청소하지 않았는지 not check[x+darr[d][0][y+darr[d][1] 를 검사하고
        if not(check[x+darr[d][0]][y+darr[d][1]] or statearr[x+darr[d][0]][y+darr[d][1]]):
            # 조건을 만족한다면 재귀적으로 청소하기 위해 그 방향으로 로봇 청소기를 이동한다. (solution 함수 호출)
            solution(x+darr[d][0], y+darr[d][1], d)
            # 로봇청소기는 하나이기 때문에 return 해줘야 한다.
            return
    # 이 statement까지 왔다는 것은 위의 for문에서 return되지 않았다는 것
    # 즉 네 방향 모두 갈 수 없었다는 뜻이기 때문에
    # 만약 로봇청소기 기준으로 뒤쪽이 벽이 아니라면 후진하여 solution 함수를 호출한다.
    if statearr[x-darr[d][0]][y-darr[d][1]] != 1:
        # 뒤로 가는 부분 수정
        solution(x-darr[d][0], y-darr[d][1], d)
        return
    # 벽이라면 그대로 정지한다. (return)
    else:
        return

solution(r, c, d)
answer = sum([sum(idx) for idx in check])
print(answer)