'''
[본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]

스노우타운에서 호텔을 운영하고 있는 스카피는 호텔에 투숙하려는 고객들에게 방을 배정하려 합니다. 호텔에는 방이 총 k개 있으며, 각각의 방은 1번부터 k번까지 번호로 구분하고 있습니다. 처음에는 모든 방이 비어 있으며 스카피는 다음과 같은 규칙에 따라 고객에게 방을 배정하려고 합니다.

한 번에 한 명씩 신청한 순서대로 방을 배정합니다.
고객은 투숙하기 원하는 방 번호를 제출합니다.
고객이 원하는 방이 비어 있다면 즉시 배정합니다.
고객이 원하는 방이 이미 배정되어 있으면 원하는 방보다 번호가 크면서 비어있는 방 중 가장 번호가 작은 방을 배정합니다.
예를 들어, 방이 총 10개이고, 고객들이 원하는 방 번호가 순서대로 [1, 3, 4, 1, 3, 1] 일 경우 다음과 같이 방을 배정받게 됩니다.

원하는 방 번호	배정된 방 번호
1	1
3	3
4	4
1	2
3	5
1	6
전체 방 개수 k와 고객들이 원하는 방 번호가 순서대로 들어있는 배열 room_number가 매개변수로 주어질 때, 각 고객에게 배정되는 방 번호를 순서대로 배열에 담아 return 하도록 solution 함수를 완성해주세요.

[제한사항]
k는 1 이상 1012 이하인 자연수입니다.
room_number 배열의 크기는 1 이상 200,000 이하입니다.
room_number 배열 각 원소들의 값은 1 이상 k 이하인 자연수입니다.
room_number 배열은 모든 고객이 방을 배정받을 수 있는 경우만 입력으로 주어집니다.
예를 들어, k = 5, room_number = [5, 5] 와 같은 경우는 방을 배정받지 못하는 고객이 발생하므로 이런 경우는 입력으로 주어지지 않습니다.
[입출력 예]
k	room_number	result
10	[1,3,4,1,3,1]	[1,3,4,2,5,6]
입출력 예에 대한 설명
입출력 예 #1

문제의 예시와 같습니다.

첫 번째 ~ 세 번째 고객까지는 원하는 방이 비어 있으므로 즉시 배정받을 수 있습니다. 네 번째 고객의 경우 1번 방을 배정받기를 원했는데, 1번 방은 빈 방이 아니므로, 1번 보다 번호가 크고 비어 있는 방 중에서 가장 번호가 작은 방을 배정해야 합니다. 1번 보다 번호가 크면서 비어있는 방은 [2번, 5번, 6번...] 방이며, 이중 가장 번호가 작은 방은 2번 방입니다. 따라서 네 번째 고객은 2번 방을 배정받습니다. 마찬가지로 5, 6번째 고객은 각각 5번, 6번 방을 배정받게 됩니다.
'''


def solution(k, room_number):
    '''
    효율성의 핵심은 같은 data를 여러 번 보지 않기
    이 문제에서는 이미 있는 것으로 확인된 room을 요청이 들어올 때마다 계속 확인한다면 비효율!
    '''
    answer = []
    nextroom = {} # key : 요청된 방 번호 / value : 요청이 들어온 방에 대해 가장 먼저 비어있는지 볼 방 번호
    for room in room_number:
        # 만약 room이 nextroom의 key에 있다면 이미 차 있는 방이라는 뜻
        if room in nextroom.keys():
            # udpatenextroom함수로 보내 다음 방을 배정받도록 한다.
            answer.append(updatenextroom(nextroom, room))
        else:
            # 없다면 배정하고
            answer.append(room)
            # nextroom dictionary에 다음으로 안내될 방 번호 (room+1)을 저장해 둔다.
            # 이 room+1가 이미 차 있는 방이라도 updatenextroom function에서 한 번 더 확인하기 때문에 괜찮다.
            nextroom[room] = room+1
        print(answer, nextroom)
    return answer

def updatenextroom(nextroom, roomnum):
    # 비어 있는 room을 만날 때까지 nextroom을 타고 간다.
    # 이 때 이미 확인한 방은 건너뛰고 다음으로 확인할 비어 있는 방이 계속 value로 update되기 때문에
    # 한 번 차 있는 것을 확인한 방은 다시 보지 않는다.
    # 혹은 한 번 배정된 방의 value는 그 방 +1의 값으로 저장된다.
    # -> 이 방은 이미 차 있으므로 다음에 들어온 고객이 이 방을 원할 경우, 이 방 (key)에 저장된 방 (value)부터 비어 있는지 확인하시오.
    if nextroom[roomnum] not in nextroom.keys():
        ans = nextroom[roomnum]
        # roomnum, ans의 nextroom을 update해준다.
        nextroom[roomnum] += 1
        # 빈 방을 찾으면 그 방에 대해서도 ans, ans+1로 저장해준다.
        nextroom[ans] = ans+1
        return ans
    else:
        nextroom[roomnum] = nextroom[nextroom[roomnum]]
        return updatenextroom(nextroom, roomnum)

# ans + 1, room + 1이 비어있다는 확신은 없지만, 저장할 때마다 계속 연쇄적으로 빈 방을 찾아서 update하는 것보다
# 요청이 들어올 때마다 update하는 것이 효율이 좋다.

solution(10, [1, 3, 4, 1, 3, 1])