from sys import stdin

n = int(stdin.readline())


def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


for i in range(n):
    a, b = map(int, stdin.readline().split())

    print(lcm(a, b))
