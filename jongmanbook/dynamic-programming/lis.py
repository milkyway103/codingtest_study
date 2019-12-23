from sys import stdin

def lis(arr):
    if not arr:
        return 0
    ret = 0
    for i in range(len(arr)):
        B = list()
        for j in range(i+1, len(arr)):
            if (arr[i] < arr[j]):
                B.append(arr[j])
        ret = max(ret, 1+lis(B))
    return ret

cache = dict()
# arr[start]에서 시작하는 증가 부분 수열 중 최대 길이를 반환
def lis2(start, n, arr):
    if start in cache.keys():
        return cache[start]
    # start가 항상 존재하기 때문에 길이는 start를 포함하여, 최하 1
    ret = 1
    for next in range(start+1, n):
        if (arr[start] < arr[next]):
            ret = max(ret, lis2(next, n, arr) + 1)
    return ret

cache = dict()
def lis3(start, n, arr):
    if start+1 in cache.keys():
        return cache[start+1]
    ret = 1
    for next in range(start+1, n):
        if (start == -1 or arr[start] < arr[next]):
            ret = max(ret, lis3(next, n, arr) + 1)
    return ret

cache = dict()
def fasterlis(n, arr):
    cache = dict()
    for idx in range(n):
        # print("befor :", cache)
        if idx == 0:
            cache[1] = arr[idx]
            continue
        updatedict = dict()
        for k, v in cache.items():
            if k ==1 and v > arr[idx]:
                updatedict[k] = arr[idx]
            if v < arr[idx] and (k+1 not in cache.keys() or cache[k+1] > arr[idx]):
                updatedict[k+1] = min(updatedict.get(k+1, float('inf')), arr[idx])
        for k, v in updatedict.items():
            cache[k] = v
        # print(idx, cache)
    return max(cache.keys())

input = stdin.readline
C = int(input())
for tc in range(C):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = fasterlis(n, arr)
    print(answer)
