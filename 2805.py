from sys import stdin

n, m = map(int, stdin.readline().split())
trees = list(map(int, stdin.readline().split()))

# for i in range(max(trees), 0, -1):
#     s = 0
#     for j in trees:
#         if j - i > 0:
#             s += j - i
#     if s == m:
#         print(i)
#         break

start, end = 0, max(trees)

while start <= end:
    mid = (start + end) // 2
    sum_tree = 0
    for i in trees:
        if i > mid:
            sum_tree += i - mid

    if sum_tree >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)
