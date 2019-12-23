import sys

def match(pattern, word):
    pos = 0
    while(pos < len(pattern) and pos < len(word) \
          and (word[pos] == '?' or word[pos] == pattern[pos])):
        pos += 1
    if pos == len(pattern):
        if len(pattern) == len(word):
            return True
    if pos == len(word):
        for patpos in range(pos, len(pattern)):
            if pattern[patpos] != '*':
                return False
            return True
    if pattern[pos] == '*':
        skip = 0
        while pos+skip <= len(word):
            if (match(pattern[pos+1:], word[pos+skip:])):
                return True
            skip += 1
    return False

# 두 문자열의 시작 위치만을 넘긴다.
cache = dict()
# 와일드카드 패턴 pattern[p...]가 문자열 word[w...]에 대응되는지 여부를 반환한다.
def matchMemoized(p, w, pattern, word):
    # 메모이제이션
    if (p, w) in cache.keys():
        return cache[(p, w)]
    # Pattern[p]와 Word[w]를 맞춰나간다.
    while w < len(word) and p < len(pattern) \
            and (pattern[p] == '?' or pattern[p] == word[w]):
        p+=1
        w+=1
    # 더이상 대응할 수 없으면 왜 while문이 끝났는지 확인한다.
    # 2. 패턴 끝에 도달해서 끝난 경우 : 문자열도 끝났어야 함
    if p == len(pattern):
        cache[(p, w)] = len(pattern) == len(word)
        return cache[(p, w)]
    # 4. *를 만나서 끝난 경우 : *에 몇 글자를 대응해야 할지 재귀 호출하면서 확인한다.
    if pattern[p] == '*':
        skip = 0
        while w + skip <= len(word):
            if (matchMemoized(w + 1, w + skip)):
                cache[(p, w)] = True
                return cache[(p, w)]
            skip += 1
    # 3. 이 외의 경우에는 모두 대응되지 않는다.
    cache[(p, w)] = False
    return cache[(p, w)]

# 다른 분해 방법
# pattern[p]와 word[w]를 맞춰나간다.
def matchMemoized2(p, w, pattern, word):
    if (p, w) in cache.keys():
        return cache[(p, w)]
    while w < len(word) and p < len(pattern) \
            and (pattern[p] == '?' or pattern[p] == word[w]):
        # p와 w를 1씩 증가시키고 계속하는 대신, 패턴과 문자열의 첫 한 글자씩을 떼고
        # 이들이 서로 대응되는지 재귀 호출로 확인할 수 있다.
        cache[(p, w)] = matchMemoized2(p+1, w+1);
        return cache[(p, w)]
    if p == len(pattern):
        cache[(p, w)] = len(pattern) == len(word)
        return cache[(p, w)]
    # 4. *를 만나서 끝난 경우 : *에 몇 글자를 대응해야 할지 재귀 호출하면서 확인한다.
    # 매 단계에서 *에 아무 글자도 대응시키지 않을 것인지,
    # 아니면 한 글자를 더 대응시킬 것인지 결정
    if pattern[p] == '*':
        if (matchMemoized(p + 1, w) or (p < len(pattern) and matchMemoized2(p, w+1))):
            cache[(p, w)] = True
            # 0글자가 대응되는 경우, 한 글자가 대응되는 경우 등을 모두 재귀 호출을 통해 확인하고 그 과정을 메모이제이션으로 캐싱
            return True
    # 3. 이 외의 경우에는 모두 대응되지 않는다.
    cache[(p, w)] = False
    return cache[(p, w)]

input = sys.stdin
C = int(input())
for tc in range(C):
    pattern = input()
    n = int(input())
    file = list()
    matched = list()
    for word in range(n):
        if match(pattern, word):
            file.append(input())
