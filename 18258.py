# from sys import stdin
#
# n = int(stdin.readline())
# queue = []
# cnt = 0
#
# for i in range(n):
#     command = stdin.readline().split()
#
#     if command[0] == 'push':
#         queue.append(int(command[1]))
#     elif command[0] == 'pop':
#         if len(queue) - cnt == 0:
#             print(-1)
#         else:
#             print(queue[cnt])
#             cnt += 1
#     elif command[0] == 'size':
#         print(len(queue) - cnt)
#     elif command[0] == 'empty':
#         if len(queue) - cnt == 0:
#             print(1)
#         else:
#             print(0)
#     elif command[0] == 'front':
#         if len(queue) - cnt == 0:
#             print(-1)
#         else:
#             print(queue[cnt])
#     elif command[0] == 'back':
#         if len(queue) - cnt == 0:
#             print(-1)
#         else:
#             print(queue[-1])


from sys import stdin
from collections import deque

n = int(stdin.readline())
queue = deque()

for i in range(n):
    command = stdin.readline().split()
    if command[0] == 'push':
        queue.append(int(command[1]))
    elif command[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
