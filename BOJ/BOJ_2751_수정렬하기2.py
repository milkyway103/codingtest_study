from sys import stdin

input = stdin.readline

N = int(input())
numbers = list()
for i in range(N):
    numbers.append(int(input()))
numbers.sort()
for i in numbers:
    print(i)