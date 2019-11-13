from sys import stdin
from collections import deque

input = stdin.readline

deqlist = list()

# 각 톱니바퀴의 최초 상태를 deque에 저장
for _ in range(4):
    temp = input()
    d = deque()
    for idx in range(8):
        d.append(int(temp[idx]))
    deqlist.append(d)
r = int(input())
rotation = [ list(map(int, input().split())) for _ in range(r)]

for x, d in rotation:
    # 돌릴 방향을 저장하는 list
    direct = [0, 0, 0, 0]
    if x==1:
        direct[0] = d
        flag = True
        idx = 1
        _d = d
        while idx<4 and flag:
            # 인접한 톱니의 극이 일치하면 연쇄작용을 멈춘다.
            if deqlist[idx][6] == deqlist[idx-1][2]:
                flag = False
            else:
                # 인접한 톱니의 극이 일치하지 않으면
                # 방향을 반대로 바꾸고
                _d = -_d
                # direct list에 저장한다.
                direct[idx] = _d
                idx += 1

    if x==2:
        direct[1] = d
        if deqlist[0][2] != deqlist[1][6]:
            direct[0] = -d
        flag = True
        idx = 2
        _d = d
        while idx<4 and flag:
            if deqlist[idx][6] == deqlist[idx-1][2]:
                flag = False
            else:
                _d = -_d
                direct[idx] = _d
                idx += 1
    if x==3:
        direct[2] = d
        if deqlist[3][6] != deqlist[2][2]:
            direct[3] = -d
        flag = True
        idx = 1
        _d = d
        while idx>=0 and flag:
            if deqlist[idx][2] == deqlist[idx+1][6]:
                flag = False
            else:
                _d = -_d
                direct[idx] = _d
                idx -= 1
    if x==4:
        direct[3] = d
        flag = True
        idx = 2
        _d = d
        while idx>=0 and flag:
            if deqlist[idx][2] == deqlist[idx+1][6]:
                flag = False
            else:
                _d = -_d
                direct[idx] = _d
                idx -= 1
    # 저장된 direct list에 맞게 방향을 돌려준다.
    for idx, xd in enumerate(direct):
        if xd != 0:
            # deque의 내장 메서드 rotate 사용
            deqlist[idx].rotate(xd)

result = 0
dx = [1, 2, 4, 8]
for idx in range(4):
    result = result + deqlist[idx][0]*dx[idx]
print(result)