from sys import stdin

input = stdin.readline
N, L = list(map(int, input().split()))
map = [ list(map(int, input().split())) for _ in range(N)]

result = 0

# 갈 수 있는 길인지 검사하는 함수
def ispossible(idx, horizontal):
    global map
    # horizontal하게 검사
    if horizontal:
        jdx = 0
        check = [False]*N
        while jdx < N-1:
            # 높이 차이가 난다면
            if map[idx][jdx] - map[idx][jdx+1] == 0:
                jdx+=1
            else:
                # 높이 차이가 1 이상이라면 갈 수 없는 길이기 때문에 False 반환
                if abs(map[idx][jdx] - map[idx][jdx + 1]) > 1:
                    return False
                prev = True
                # 앞 블록이 더 낮으면 True, 높으면 Flase가 저장되는 변수 prev
                if map[idx][jdx] > map[idx][jdx+1]:
                    prev = False
                if prev:
                    # 앞 블록이 더 낮을 때는 자기 자신을 포함해서 경사로를 놓아야 한다
                    for l in range(L):
                        if jdx -l < 0 :
                            return False
                        if map[idx][jdx-l] != map[idx][jdx]:
                            return False
                        # 이미 경사로가 있다면
                        if check[jdx-l] == True:
                            return False
                        check[jdx-l] = True
                    jdx += 1
                else:
                    # 뒷 블록이 더 낮을 때는 자기 자신은 제외하고 그 뒤부터 경사로를 놓아야 한다
                    for l in range(1, L+1):
                        if jdx+l >= N:
                            return False
                        if map[idx][jdx+l] != map[idx][jdx+1]:
                            return False
                        check[jdx+l] = True
                    jdx += L

    # vertical하게 검사
    else:
        jdx = idx
        idx = 0
        check = [False]*N
        while idx < N-1:
            # 높이 차이가 난다면
            if map[idx][jdx] - map[idx+1][jdx] == 0:
                idx+=1
            else:
                # 높이 차이가 1 이상이라면 갈 수 없는 길이기 때문에 False 반환
                if abs(map[idx][jdx] - map[idx+1][jdx]) > 1:
                    return False
                prev = True
                # 앞 블록이 더 낮으면 True, 높으면 Flase가 저장되는 변수 prev
                if map[idx][jdx] > map[idx+1][jdx]:
                    prev = False
                if prev:
                    # 앞 블록이 더 낮을 때는 자기 자신을 포함해서 경사로를 놓아야 한다
                    for l in range(L):
                        if idx - l < 0:
                            return False
                        if map[idx-l][jdx] != map[idx][jdx]:
                            return False
                        # 이미 경사로가 있다면
                        if check[idx - l] == True:
                            return False
                        check[idx - l] = True
                    idx += 1
                else:
                    # 뒷 블록이 더 낮을 때는 자기 자신은 제외하고 그 뒤부터 경사로를 놓아야 한다
                    for l in range(1, L + 1):
                        if idx + l >= N:
                            return False
                        if map[idx+l][jdx] != map[idx+1][jdx]:
                            return False
                        check[idx + l] = True
                    idx += L
    return True


# 모든 가능한 길에 대하여
for idx in range(N):
    if ispossible(idx, True):
        result += 1
    if ispossible(idx, False):
        result += 1

print(result)

