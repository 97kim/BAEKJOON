from sys import stdin

n = int(stdin.readline())

lst = []

for i in range(n):
    x, y = map(int, stdin.readline().split())
    lst.append([x, y])

lst.sort(key=lambda k: (k[1], k[0]))

for j in lst:
    print(j[0], j[1])
