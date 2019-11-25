def solution(stones, k):
    # k, 즉 한 번에 뛰어넘을 수 있는 돌의 개수가 1인 경우에는 돌들 중 하나라도 0이 되면 건너갈 수 없게 되므로
    # stones의 최솟값을 return한다.
    if k == 1:
        return min(stones)

    # 그 외에는 k개의 돌들 중 가장 큰 값의 최솟값을 return

    # premaxidx와 answer의 첫 번째 stone으로 초기화
    premaxidx = 0
    answer = stones[premaxidx]

    # 첫 k개까지의 돌들 중에서 max값인 stone의 idx를 premaxidx에 저장
    for idx in range(1, k):
        if stones[premaxidx] <= stones[idx]:
            premaxidx = idx
            # 이때 answer도 함께 update
            answer = stones[premaxidx]

    # 모든 stones를 돌면서
    for idx in range(1, len(stones)):
        if idx + k > len(stones):
            break
        # 이미 확인한 idx라면 건너뛴다.
        if premaxidx == idx:
            continue
        # 지금 확인하고 있는 idx가 premaxidx보다 더 작고 (앞의 인덱스이고)
        # stone의 수가 같거나 크다면
        # premaxidx와 answer를 update하고
        if premaxidx > idx:
            if stones[premaxidx] <= stones[idx]:
                premaxidx = idx
                answer = min(stones[premaxidx], answer)
        # 지금 확인하고 있는 idx가 premaxidx보다 같거나 크다면 premaxidx를 다시 계산하여 update해야 한다.
        else:
            premaxidx = idx
            for jdx in range(idx + 1, idx + k):
                if stones[premaxidx] <= stones[jdx]:
                    premaxidx = jdx
            answer = min(stones[premaxidx], answer)
    return answer