from sys import stdin
import itertools

# Input
input = stdin.readline
N = int(input())
A = list(map(int, input().split()))
operators = list(map(int, input().split()))

# 연산자들의 리스트 만들기
pools = ['+']*operators[0] + ['-']*operators[1] + ['*']*operators[2] + ['%']*operators[3]
# 주어진 연산자들로 순열 생성 <= itertools의 순열을 생성해주는 함수 사용
operatorspermu = list(map(''.join, itertools.permutations((pools))))
# 중복 제거
operatorspermu = list(set(operatorspermu))

# 최솟값, 최댓값 초기화 (-10억과 10억 사이)
minans = 1000000000
maxans = -1000000000

# 모든 가능한 연산자 조합에 대해
for operator in operatorspermu:
    queue = list()
    opnum = 0
    # 숫자 리스트를 돌면서
    for op in A:
        # queue가 0이면 그냥 숫자를 넣어주고
        if len(queue) == 0:
            queue.append(op)
        # 아니라면 연산 진행
        else:
            # x는 queue에서 pop하고
            x = queue.pop(0)
            # y는 이번 숫자
            y = op
            # 연산자를 꺼내 주고
            oper = operator[opnum]
            # opnum은 다음에 꺼낼 연산자를 위해 +1 해준다
            opnum += 1
            # 각 연산자에 대해 알맞은 연산 진행
            if oper == '+':
                queue.append(x+y)
            elif oper == '-':
                queue.append(x-y)
            elif oper == '*':
                queue.append(x*y)
            else:
                # 나눗셈인 경우 x가 음수이고 y가 양수인 경우 조건에 맞게 처리
                if x < 0 and y > 0:
                    x = -x
                    res, _ = divmod(x, y)
                    res = -res
                    queue.append(res)
                else:
                    res, _ = divmod(x, y)
                    queue.append(res)
    # 최솟값과 최댓값 갱신
    minans = min(minans, queue[0])
    maxans = max(maxans, queue[0])

# 최종적으로 프린트
print(maxans)
print(minans)

