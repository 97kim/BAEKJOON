num = input()
initial_num = num
count = 0

if int(num) < 10:
    num = '0' + num
    initial_num = num

while True:
    result = str(int(num[0]) + int(num[1]))
    num = num[1] + result[-1]
    count += 1
    if initial_num == num:
        break

print(count)