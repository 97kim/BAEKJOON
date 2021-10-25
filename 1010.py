# 조합 이항계수 nCm = m! / (n! * (m - n)!)

from sys import stdin


def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


cycle = int(stdin.readline())

for _ in range(cycle):
    n, m = map(int, stdin.readline().split())
    print(factorial(m) // (factorial(n) * factorial(m - n)))
