import sys

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
