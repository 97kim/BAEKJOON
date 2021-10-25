# num_list = []
# a = int(input())
#
# for i in range(a):
#     num = int(input())
#     if num != 0:
#         num_list.append(num)  # 리스트의 마지막 원소 추가
#     else:
#         num_list.pop()  # 리스트의 마지막 원소 제거
# print(sum(num_list))


from sys import stdin

num_list = []
a = int(stdin.readline())

for i in range(a):
    num = int(stdin.readline())
    if num != 0:
        num_list.append(num)
    else:
        num_list.pop()
print(sum(num_list))
