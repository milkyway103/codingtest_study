from sys import stdin

input = stdin.readline

def powerset(seq):
    if len(seq) < 1:
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]] + item
            yield item

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
numbersset = list()
for item in powerset(numbers):
    if item == []:
        continue
    numbersset.append(item)
answer = len([1 for idx in numbersset if sum(idx) == S])
print(answer)