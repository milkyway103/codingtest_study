def solution(food_times, k):
    answer = 0
    foodcounts = len(food_times)
    temp = list()
    for idx in range(foodcounts):
        temp.append(0)
    thisfood = 0
    time = 0

    queue = list()
    while food_times != temp:
        for idx, _ in enumerate(food_times):
            queue.insert(0, idx + 1)
            food_times[idx] -= 1

    while queue and time < k:
        thisfood = queue.pop()
        print(thisfood)
        time += 1
        if time == k:
            return thisfood

    return -1

solution([3, 1, 2], 5)