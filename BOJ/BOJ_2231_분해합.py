N = int(input())

answer = 0
for idx in range(1, N):
    idxlist = [int(_) for _ in str(idx)]
    temp = idx + sum(idxlist)
    if temp == N:
        answer = idx
        break
print(answer)