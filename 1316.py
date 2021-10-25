from sys import stdin

n = int(stdin.readline())
count = n

for a in range(n):
    str_input = stdin.readline().strip()
    print(str_input)
    for i in range(len(str_input) - 1):
        if str_input[i] == str_input[i + 1]:
            continue
        elif str_input[i] in str_input[i + 1:]:
            count -= 1
            break
print(count)
