str_input = input().upper()

count_list = [0] * 26

for char in str_input:
    idx = ord(char) - 65  # 65 == ord('A')
    count_list[idx] += 1

count = 0

for n in count_list:
    if n == max(count_list):
        count += 1

if count > 1:
    print('?')
else:
    for i in range(len(count_list)):
        if count_list[i] == max(count_list):
            print(chr(i + 65))  # 65 == ord('A')
