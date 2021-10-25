# a, b, c = map(int, input().split())
# day = 0
# height = 0

# while True:
#     day += 1
#     height += a
#     if height >= c - a:
#         print(day)
#         break
#     height -= b

a, b, c = map(int, input().split())

day = (c - b) // (a - b)
if (c - b) % (a - b) == 0:
    print(day)
else:
    print(day + 1)
