from sys import stdin

input = stdin.readline

dirdict = {'U':0, 'F':1, 'D':2, 'B':3, 'L':4, 'R':5}
wisedict = {'-':-1, '+':1}
arr = list()

for _ in range(int(input())):
    for _ in range(int(input())):
        tmp = input().split()
        arr.extend([(dirdict[d], wisedict[c]) for d, c in tmp])

cube = [[['w']*3 for _ in range(3)],
        [['r']*3 for _ in range(3)],
        [['y']*3 for _ in range(3)],
        [['o']*3 for _ in range(3)],
        [['g']*3 for _ in range(3)],
        [['b']*3 for _ in range(3)]]


