from sys import stdin
all_count = int(stdin.readline())

result = []

for i in range(all_count):
    count = 0
    input_case = list(map(int, stdin.readline().split()))
    avg = sum(input_case[1:]) / input_case[0]

    for j in input_case[1:]:
        if j > avg:
            count += 1
    result.append(count / input_case[0] * 100)

for r in result:
    print("{:.3f}%".format(r))
