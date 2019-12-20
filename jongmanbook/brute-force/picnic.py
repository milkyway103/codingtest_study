from sys import stdin

# def countPairings(taken, n, areFriends):
#     finished = True;
#     for idx in range(n):
#         if not taken[idx]:
#             finished = False
#     if finished:
#         return 1
#     ret = 0
#     for idx in range(n):
#         for jdx in range(n):
#             if not taken[idx] and not taken[jdx] and areFriends[idx][jdx]:
#                 taken[idx] = taken[jdx] = True
#                 ret += countPairings(taken, n, areFriends)
#                 taken[idx] = taken[jdx] = False
#     return ret

def countPairings(taken, n, areFriends):
    # 남은 학생들 중 가장 번호가 빠른 학생을 찾는다.
    firstFree = -1
    for idx in range(n):
        if not taken[idx]:
            firstFree = idx
            break
    # 기저 사례 : 모든 학생이 짝을 찾았으면 한 가지 방법을 찾았으니 종료한다.
    if firstFree == -1:
        return 1
    ret = 0
    # 이 학생과 짝지을 학생을 결정한다.
    for pairWith in range(firstFree+1, n):
        if not taken[pairWith] and areFriends[firstFree][pairWith]:
            taken[firstFree] = taken[pairWith] = True
            ret += countPairings(taken, n, areFriends)
            taken[firstFree] = taken[pairWith] = False
    return ret

input = stdin.readline
C = int(input())

for _ in range(C):
    answer = 0
    n, m = list(map(int, input().split()))
    areFriends = [[False]*n for _ in range(n)]
    temp_friends = list(map(int, input().split()))
    for idx in range(m):
        areFriends[temp_friends[idx*2]][temp_friends[idx*2+1]] = True
        areFriends[temp_friends[idx*2+1]][temp_friends[idx*2]] = True
    taken = [False]*n
    print(countPairings(taken, n, areFriends))

