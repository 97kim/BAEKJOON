from sys import stdin


def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


a, b = map(int, stdin.readline().split())

print(gcd(a, b))
print(lcm(a, b))

# a, b = map(int, stdin.readline().split())
#
# for i in range(1, min(a, b) + 1):
#     if min(a, b) % i == 0 and max(a, b) % i == 0:
#         great = i
#
# least = great * (a // great) * (b // great)
#
# print(great)
# print(least)