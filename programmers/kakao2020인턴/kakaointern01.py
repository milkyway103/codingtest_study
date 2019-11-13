'''

'''
from collections import deque

def solution(board, moves):
    answer = 0
    basket = deque()
    new_board = [deque() for _ in range(len(board))]
    for line in board[::-1]:
        for idx, item in enumerate(line):
            if item != 0:
                new_board[idx].append(item)
    for grab in moves:
        try:
            this_item = new_board[grab-1].pop()
            if basket and basket[-1] == this_item:
                answer += 2
                basket.pop()
            else:
                basket.append(this_item)
        except IndexError:
            continue
    return answer