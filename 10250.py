from sys import stdin

# cycle = int(stdin.readline())
#
# for i in range(cycle):
#     rooms = []
#     h, w, n = map(int, stdin.readline().split())
#
#     for j in range(1, w + 1):
#         for k in range(1, h + 1):
#             rooms.append(k * 100 + j)
#     print(rooms[n - 1])


cycle = int(stdin.readline())

for i in range(cycle):
    h, w, n = map(int, input().split())
    floor = n % h
    room = (n // h) + 1
    if n % h == 0:
        floor = h
        room = n // h
    print(floor * 100 + room)
