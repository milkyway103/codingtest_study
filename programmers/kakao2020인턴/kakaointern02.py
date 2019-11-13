def solution(s):
    answer = []
    tuples = []
    s = s[2:-2]
    s = s.split('},{')
    for idx, line in enumerate(s):
        s[idx] = list(map(int, line.split(',')))
    s.sort(key = lambda x: len(x))
    for items in s:
        for item in items:
            if item not in answer:
                answer.append(item)
                break
    return answer