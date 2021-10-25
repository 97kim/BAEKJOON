from sys import stdin


def check_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


repo = []

for j in range(2, 246912):  # 1 <= n <= 123456
    if check_prime(j):
        repo.append(j)

while True:
    n = int(stdin.readline())
    count = 0

    if n == 0:
        break
    for k in repo:
        if n < k <= n * 2:
            count += 1
    print(count)
