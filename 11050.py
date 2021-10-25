n, k = map(int, input().split())


# def factorial(a):
#     if a == 1:
#         return 1
#
#     return a * factorial(a-1)

def factorial(a):
    result = 1
    for i in range(1, a + 1):
        result *= i
    return result


print(factorial(n) // (factorial(k) * factorial(n-k)))
