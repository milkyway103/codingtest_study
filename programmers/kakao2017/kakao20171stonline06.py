def solution(m, n, board):
    newboard = list()
    for idx, line in enumerate(board):
        newboard.append([item for item in line])
    return match(m, n, newboard)

def match(m, n, newboard):
    matchlist = list()
    for idx in range(m-1):
        for jdx in range(n-1):
            if newboard[idx][jdx] == 1:
                continue
            if newboard[idx][jdx] == newboard[idx][jdx+1] and \
                newboard[idx][jdx] == newboard[idx+1][jdx] and \
                newboard[idx][jdx] == newboard[idx+1][jdx+1]:
                # print(idx, jdx)
                matchlist.extend([[idx, jdx], [idx, jdx+1], \
                                 [idx+1, jdx], [idx+1, jdx+1]])
    if len(matchlist) == 0:
        return countone(m, n, newboard)
    else:
        newboard = dropblock(m, n, newboard, matchlist)
        return match(m, n, newboard)

def dropblock(m, n, newboard, matchlist):
    for idx in matchlist:
        newboard[idx[0]][idx[1]] = 1
    for jdx in range(n):
        for idx in range(m-1):
            if newboard[idx][jdx] != 1 and newboard[idx+1][jdx] == 1:
                newboard[idx][jdx], newboard[idx+1][jdx] = \
                    newboard[idx+1][jdx], newboard[idx][jdx]
    return newboard

def countone(m, n, board):
    result = 0
    for idx in range(m):
        for jdx in range(n):
            if board[idx][jdx] == 1:
                result += 1
    return result



board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(6, 6, board)) # answer : 15
board2 = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(4, 5, board2))
