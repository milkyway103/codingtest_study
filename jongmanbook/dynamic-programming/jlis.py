from sys import stdin

minvalue = -float('inf')
def jlis(indexA, indexB):
    '''
    :param indexA: 탐색을 시작할 A의 index
    :param indexB: 탐색을 시작할 B의 index
    :return: min(A[indexA], B[indexB]), max(A[indexA], B[indexB])로 시작하는
     합친 증가 부분 수열의 최대 길이
     단 indexA == indexB == -1 혹은 A[indexA] != B[indexB]라고 가정
    '''
    global A, B, n, m, cache
    if (indexA, indexB) in cache.keys():
        return cache[(indexA, indexB)]
    # A[indexA], B[indexB]가 이미 존재하므로 2개는 항상 있다.
    ret = 2
    a = minvalue if indexA == -1 else A[indexA]
    b = minvalue if indexB == -1 else B[indexB]
    maxElement = max(a, b)
    # 두 수열을 돌면서 다음 원소를 찾는다.
    for nextA in range(indexA+1, n):
        if maxElement < A[nextA]:
            ret = max(ret, jlis(nextA, indexB) + 1)
    for nextB in range(indexB+1, m):
        if maxElement < B[nextB]:
            ret = max(ret, jlis(indexA, nextB) + 1)
    cache[(indexA, indexB)] = ret # 계산한 값을 cache에 저장한다.
    return ret


input = stdin.readline
C = int(input())
for _ in range(C):
    cache = dict()
    n, m = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(jlis(-1, -1) - 2)
