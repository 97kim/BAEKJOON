numbers_range = list(range(1, 10001))
self_number_list = []

for number in numbers_range:
    for n in str(number):
        number += int(n)
    if number <= 10000:
        self_number_list.append(number)

for self_number in set(self_number_list):
    numbers_range.remove(self_number)

for result in numbers_range:
    print(result)
