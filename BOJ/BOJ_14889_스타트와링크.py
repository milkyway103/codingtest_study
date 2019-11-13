from sys import stdin

input = stdin.readline

N = int(input())
s = [list(map(int, input().split())) for _ in range(N)]
# 팀1에 속했는지 check해주기 위한 배열
check = [False]*N
minans = 1e9

def solution(cnt, idx):
    global minans
    # idx가 N과 같다면 out of range이므로 return
    if idx == N:
        return
    # 팀의 반을 선택했다면 팀의 전력 계산
    if cnt == N//2:
        s1, s2 = 0, 0
        for i in range(N):
            for j in range(N):
                if check[i] and check[j]:
                    s1 += s[i][j]
                if not check[i] and not check[j]:
                    s2 += s[i][j]
        # 최솟값 갱신
        minans = min(minans, abs(s1-s2))
        return
    # 백트래킹
    check[idx] = True
    solution(cnt+1, idx+1)
    check[idx] = False
    solution(cnt, idx+1)

solution(0, 0)
print(minans)