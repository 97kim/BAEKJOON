from sys import stdin

a = int(stdin.readline())
divisor = list(map(int, stdin.readline().split()))

print(min(divisor) * max(divisor))
