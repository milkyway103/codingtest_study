# 재귀적으로 만들기
def perm(arr, depth, n, k):
    # depth가 0부터 시작하여 k라면 k개를 모두 뽑은 것이므로 print하고 return
    if (depth == k):
        print(arr)
        return
    for idx in range(depth, n):
        # 각 depth에 대해 남아 있는 것들 중에 모두 뽑아보고,
        # 해당 경우에 대해 재귀적으로 perm 함수를 돌리고,
        # 원상복구 하여 다시 경우의 수를 찾는다
        arr[idx], arr[depth] = arr[depth], arr[idx]
        perm(arr, depth+1, n, k)
        arr[idx], arr[depth] = arr[depth], arr[idx]

# 리니어하게 만들기
def permute(arr):
    # 입력받은 array를 swallow copy (우선 자기 자신을 넣는다.)
    result = [arr[:]]
    # 입력받은 array의 길이만큼 0으로 초기화된 배열 c를 생성
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        # i 시점에서 모든 경우의 수에 대해서 다 해보지 않았다면
        if c[i] < i:
            if i % 2 == 0:
                # arr의 0번째 원소와 i번째 원소를 swap
                arr[0], arr[i] = arr[i], arr[0]
            else:
                # arr의 c[i]번째 원소와 i번째 원소를 swap
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            # swap할 때마다 append해준다. (swallow copy를 해서)
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result