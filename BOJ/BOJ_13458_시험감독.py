from sys import stdin

input = stdin.readline
N = int(input())
A = map(int, list(input().split()))
B, C = map(int, list(input().split()))

def cal():
    answer = 0
    for idx in A:
        idx = idx-B
        answer += 1
        if idx > 0:
            tmp, _ = divmod(idx, C)
            if _:
                tmp+=1
            answer += tmp
    print(answer)
    return

cal()
