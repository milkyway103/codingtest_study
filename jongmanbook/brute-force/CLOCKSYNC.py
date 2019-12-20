from sys import stdin
input = stdin.readline
'''
시계 맞추기 문제를 해결하는 완전 탐색 알고리즘
'''
INF = 9999
SWITCHES = 10
CLOCKS = 16
# linked[idx][jdx] = 'x' : idx번 스위치와 jdx번 시계가 연결되어 있다.
# linked[idx][jdx] = '.' : idx번 스위치와 jdx번 시계가 연결되어 있지 않다.
linked = [
    'xxx.............',
    '...x...x.x.x....',
    '....x.....x...xx',
    'x...xxxx........',
    '......xxx.x.x...',
    'x.x...........xx',
    '...x..........xx',
    '....xx.x......xx',
    '.xxxxx..........',
    '...xxx...x...x..',
]
def areAligned(clocks):
    '''
    :param clocks: 현재 시계들의 상태
    :return: 모든 시계가 12시를 가리키고 있는지 확인
    '''
    for clock in clocks:
        if clock != 12:
            return False
    return True

def push(clocks, swtch):
    '''
    swtch번 스위치를 누른다.
    :param clocks: 현재 시계들의 상태
    :param swtch: 이번에 누를 스위치의 번호
    '''
    for idx, clock in enumerate(clocks):
        if linked[swtch][idx] == 'x':
            clocks[idx] = clocks[idx]+3
            if clocks[idx] == 15:
                clocks[idx] = 3

def solve(clocks, swtch):
    '''
    :param clocks: 현재 시계들의 상태
    :param swtch: 이번에 누를 스위치의 번호
    :return: 남은 스위치들을 눌러서 clocks를 12시로 맞출 수 있는 최소 횟수를 반환한다.
    만약 불가능하다면 INF이상의 큰 수를 반환한다.
    '''
    if(swtch == SWITCHES):
        if areAligned(clocks):
            return 0
        else:
            return INF
    # 이 스위치를 0번 누르는 경우부터 세 번 누르는 경우까지를 모두 시도한다.
    ret = INF
    for cnt in range(4):
        ret = min(ret, cnt+solve(clocks, swtch + 1))
        push(clocks, swtch)
    # solve함수를 먼저 부르고 push하는 이유 : solve함수를 부른 시점과 나온 시점의 clock 모양이 같아야
    # 오작동하지 않는다.
    # 만약 push가 먼저라면 return되는 시점에 다른 모양의 clock이 return된다.
    # push(clocks, swtch)가 네 번 호출되었으니 clocks는 원래와 같은 상태가 된다.
    return ret

def solution():
    clocks = list(map(int, input().split()))
    ans = solve(clocks, 0)
    if ans == INF:
        print(-1)
    else:
        print(ans)

def main():
    C = int(input())
    for TC in range(C):
        solution()

main()