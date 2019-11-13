from sys import stdin

input = stdin.readline

N = int(input())
consultarr = [ list(map(int, input().split())) for _ in range(N)]
result = 0

def solution(depth, temp):
    global result
    # 만약 들어온 depth가 N보다 크면 퇴사일인 것이므로 result와 비교해서 저장한다.
    if depth == N:
        result = max(result, temp)
        return
    # depth일자에 잡힌 상담이 걸리는 날짜 수를 days에 저장한다.
    days = consultarr[depth][0]
    # 만약 하루가 걸린다면 보수를 더해서 solution 함수에 보낸다.
    if days == 1:
        temp+=consultarr[depth][1]
        solution(depth+1, temp)
    # 만약 하루 이상이 걸린다면
    elif consultarr[depth][0] > 1:
        # 1) 걸리는 days의 중간 날짜로 보수를 더하지 않고 solution 함수를 탐색한다.
        for day in range(1, days):
            if depth+day > N:
                continue
            solution(depth+day, temp)
        # 2) 걸리는 days만큼 더한 후 보수를 더해서 solution 함수를 탐색하되
        # 만약 현재 날짜와 days를 더한 값이 N보다 크다면 (즉, 퇴사일까지 수행할 수 없는 일이라면
        # 보수를 더하지 않고 result와 비교해서 저장한다.
        if depth+days > N:
            result = max(result, temp)
            return
        temp += consultarr[depth][1]
        solution(depth+days, temp)

solution(0, 0)
print(result)
