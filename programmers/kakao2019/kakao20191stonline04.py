def solution(words, queries):
    # dictionary로 Trie를 만들되, length에 의한 Trie를 만들어 검색의 효율성 높임
    # 0번째 dictionary는 prefix를 위함, 1번째 dictionary는 postfix를 위함
    trie_by_length = [({}, {}) for _ in range(10001)]
    for word in words:
        length = len(word)
        t = trie_by_length[length][0]
        for c in word:
            # get(key[, default]) -> key값이 있다면 해당 value, 없다면 default 반환
            # 모든 Trie, subTrie에 대하여 'count'라는 key값을 주어 검색의 효율성 높임
            t['count'] = t.get('count', 0) + 1
            # setdefault(key[, default]) -> key값이 있다면 해당 value를 사용,
            # 없다면 default를 value로 사용
            t.setdefault(c, {})
            t = t[c]
        t = trie_by_length[length][1]
        # word를 뒤집어 postfix를 위한 Trie 생성
        for c in word[::-1]:
            t['count'] = t.get('count', 0) + 1
            t.setdefault(c, {})
            t = t[c]
    ans = []
    for query in queries:
        length = len(query)
        if query[0] == '?':
            t = trie_by_length[length][1]
            # postfix를 찾는 것이라면 query를 뒤집음
            query = query[::-1]
        else:
            t = trie_by_length[length][0]
        # 찾는 건 똑같이 찾으면 ok
        for c in query:
            if c == '?':
                ans.append(t.get('count', 0))
                break
            if c not in t:
                ans.append(0)
                break
            t = t[c]
    return ans

# 출처 : https://www.snoopybox.co.kr/2054