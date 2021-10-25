m, n = map(int, input().split())


# num 이하의 소수 구하기
def check_prime(num):
    sieve = [True] * (num + 1)

    for i in range(2, int(num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i + i, num + 1, i):
                sieve[j] = False

    return [i for i in range(2, num + 1) if sieve[i]]


for a in check_prime(n):
    if a >= m:
        print(a)
