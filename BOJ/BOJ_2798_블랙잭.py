from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))
answer = 0
# cardssum = [sum(cards[idx:idx+3]) for idx, _ in enumerate(cards[:-2]) if sum(cards[idx:idx+3])<=M]
for idx in range(0, N-2):
    for jdx in range(idx+1, N-1):
        for kdx in range(jdx+1, N):
            if cards[idx]+cards[jdx]+cards[kdx] <= M and cards[idx]+cards[jdx]+cards[kdx] > answer:
                answer = cards[idx]+cards[jdx]+cards[kdx]
print(answer)