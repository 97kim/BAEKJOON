# a = input()
# b = input()
#
# print(int(a) * int(b[2]))
# print(int(a) * int(b[1]))
# print(int(a) * int(b[0]))
# print(int(a) * int(b))

a = input()
b = input()

result = []

for i in b:
    result.insert(0, int(a) * int(i))

for answer in result:
    print(answer)

print(int(a) * int(b))