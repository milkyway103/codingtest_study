def solution(stones, k):
    if k == 1:
        return min(stones)

    answer = float('inf')
    premaxidx = 0
    for idx in range(1, k):
        if stones[premaxidx] <= stones[idx]:
            premaxidx = idx
            answer = stones[premaxidx]

    for idx in range(1, len(stones)):
        if idx + k > len(stones):
            break
        if premaxidx == idx:
            continue
        if premaxidx > idx:
            if stones[premaxidx] <= stones[idx]:
                premaxidx = idx
                answer = min(stones[premaxidx], answer)
        else:
            premaxidx = idx
            for jdx in range(idx + 1, idx + k):
                if stones[premaxidx] <= stones[jdx]:
                    premaxidx = jdx
            answer = min(stones[premaxidx], answer)
    return answer