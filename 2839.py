weight = int(input())

result = 0

if weight > 5:
    for i in range(weight // 5, -1, -1):
        m = weight - (i * 5)
        if m % 3 == 0:
            result = i + (m // 3)
            print(result)
            break
    if result == 0:
        print(-1)
elif weight == 5 or weight == 3:
    print(1)
else:
    print(-1)
