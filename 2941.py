str_input = input()

cro_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for c in cro_list:
    str_input = str_input.replace(c, '*')

print(len(str_input))