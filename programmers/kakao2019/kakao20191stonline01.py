# 내 풀이
def solution(s):
    answer = len(s)
    # 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return
    for unit in range(1, len(s) // 2 + 1):
        compressed = 0
        cur = 0
        while cur < len(s):
            # cur에 unit 길이를 더한 것이 s의 길이를 초과하는 경우 handling
            if cur + unit >= len(s):
                compressed = compressed + (len(s) - cur)
                break
            # 두 인접한 단어가 같으면
            if s[cur: cur + unit] == s[cur + unit: cur + unit * 2]:
                temp = s[cur: cur + unit]
                num = 0
                # 계속 그 인접한 다음 단어를 비교해가다가 다른 단어가 나오면 compressed에 지금까지 센 값을 더해준다.
                while temp == s[cur: cur + unit]:
                    num += 1
                    cur = cur + unit
                compressed = compressed + len(str(num)) + len(temp)
            # 다르면 그냥 더해주고 다음 단어로 넘어간다.
            else:
                # cur에 unit 길이를 더한 것이 s의 길이를 초과하는 경우 handling
                if cur + unit >= len(s):
                    compressed = compressed + (len(s) - cur)
                    break
                compressed += unit
                cur += unit
        answer = min(compressed, answer)

    return answer

# 다른 분(고재관 님)의 더 깔끔한 풀이 - list comprehension, zip 사용, 코드 구조화, TDD
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    # tok_len으로 text를 split하여 list comprehension한 것을 words에 넣어줌
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        # aabbaccc -> [('a', 'a'), ('a', 'b'), ('b', 'b'), ('b', 'a'), ('a', 'c'), ('c', 'c'), ('c', 'c'), ('c', '')]
        if a == b:
            cur_cnt += 1
        else:
            # 인접한 두 split된 문자열이 다를 경우 cur_word와 지금까지 센 숫자를 res에 넣어준다.
            res.append([cur_word, cur_cnt])
            # cur_word와 cur_cnt 갱신
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)
            # cnt가 1보다 클 경우에만 포함시켜서 sum

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))