# 하노이탑

def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return

    hanoi(n - 1, start, 6 - start - end)
    print(start, end)
    hanoi(n - 1, 6 - start - end, end)


count = int(input())
print(2 ** count - 1)
hanoi(count, 1, 3)
