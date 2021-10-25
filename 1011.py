from sys import stdin

n = int(stdin.readline())

for i in range(n):
    x, y = map(int, stdin.readline().split())

    distance = y - x
    count = 0
    move = 1
    sum_move = 0

    while sum_move < distance:
        count += 1
        sum_move += move
        if count % 2 == 0:
            move += 1
    print(count)

