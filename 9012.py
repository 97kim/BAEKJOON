from sys import stdin

n = int(stdin.readline())

for i in range(n):
    vps = stdin.readline().strip()
    while '()' in vps:
        vps = vps.replace('()', '')
    if len(vps) == 0:
        print('YES')
    else:
        print('NO')

# for i in range(n):
#     vps = stdin.readline().strip()
#     for j in range(len(vps) // 2):
#         vps = vps.replace('()', '')
#         if len(vps) == 0:
#             print('YES')
#             break
#     if len(vps) != 0:
#         print('NO')
