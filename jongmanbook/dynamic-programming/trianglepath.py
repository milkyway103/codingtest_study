```
1. 입력을 tri라는 list()에 저장해 둔다.
2. 다음과 같은 점화식이 성립한다.
try[x][y]의 부분 최적해 = try[x][y] + try[x+1][pos]의 부분 최적해
여기서 pos는 y 또는 y+1이다. (바로 아래 혹은 오른쪽 아래로만 내려갈 수 있기 때문)
그렇기 때문에 아래에서부터 부분 최적해를 찾아 위로 더해 가며 올라온다! (tri를 뒤집어 생각하면 편리)
```

from sys import stdin

input = stdin.readline
C = int(input())
for tc in range(C):
    n = int(input())
    tri = list()
    for _ in range(n):
        tri.append(list(map(int, input().split())))
    for x in range(n-2, -1, -1):
        for y in range(0, len(tri[x])):
            tri[x][y] += max(tri[x+1][y], tri[x+1][y+1])
    print(tri[0][0])
