from sys import stdin


# num 이하의 소수 구하기
def check_prime(num):
    sieve = [True] * (num + 1)

    for i in range(2, int(num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i + i, num + 1, i):
                sieve[j] = False

    return [i for i in range(2, num + 1) if sieve[i]]


repo = check_prime(123456 * 2)

while True:
    n = int(stdin.readline())
    count = 0
    if n == 0:
        break
    for k in repo:
        if n < k <= n * 2:
            count += 1
    print(count)
